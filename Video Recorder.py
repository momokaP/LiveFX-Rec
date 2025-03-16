import cv2 as cv
import tkinter as tk
from tkinter import filedialog, messagebox
import os

root = tk.Tk()
root.withdraw()

video_file = 'temp'
target_file = None
target_format = 'avi'
target_fourcc = 'XVID'

record = False
filter_mode = 0
filter_len = 4

video = cv.VideoCapture(0)

def get_unique_filename(base_name, extension):
    """ 중복되지 않는 파일명을 찾아 반환 with chapGPT """
    count = 1
    new_filename = f"{base_name}.{extension}"
    
    while os.path.exists(new_filename):  # 파일이 존재하면 이름 변경
        new_filename = f"{base_name}_{count}.{extension}"
        count += 1
    
    return new_filename

def apply_filter(img, mode):
    """ OpenCV 필터 적용 with chapGPT """
    if mode == 1:  # 흑백
        return cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    elif mode == 2:  # 블러
        return cv.GaussianBlur(img, (15, 15), 0)
    elif mode == 3:  # 엣지 감지
        return cv.Canny(img, 100, 200)
    return img  # 기본 영상 유지

if video.isOpened():
    target = cv.VideoWriter()

    fps = video.get(cv.CAP_PROP_FPS)
    if fps == 0:
        fps = 30

    wait_msec = int(1000 / fps)

    while True:
        valid, img = video.read()
        if not valid:
            break       

        if record and not target.isOpened():
            target_file = get_unique_filename(video_file, target_format)
            h, w, *_ = img.shape
            is_color = (img.ndim > 2) and (img.shape[2] > 1)
            target.open(target_file, cv.VideoWriter_fourcc(*target_fourcc), fps, (w, h), is_color)

        # 필터 적용
        filtered_img = apply_filter(img, filter_mode)
        if len(filtered_img.shape) == 2:  # 흑백 또는 엣지 감지는 컬러로 변환 필요
            filtered_img = cv.cvtColor(filtered_img, cv.COLOR_GRAY2BGR)

        if record:
            target.write(filtered_img)

            h, w, *_ = filtered_img.shape
            circle_radius = 30
            center = (w//2, h-(circle_radius+circle_radius))
            cv.circle(filtered_img, center, radius=circle_radius, color=(0, 0, 255), thickness=5)
            
            info = 'Record'
            cv.putText(filtered_img, info, (0, 30), cv.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), thickness=3)
            cv.putText(filtered_img, info, (0, 30), cv.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255))
        else:
            info = 'Preview'
            cv.putText(filtered_img, info, (0, 30), cv.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), thickness=3)
            cv.putText(filtered_img, info, (0, 30), cv.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0))
            
            if target.isOpened():
                target.release()
                
                save_video = messagebox.askyesno("저장 확인", "녹화된 영상을 저장하시겠습니까?")
                if save_video:
                    file_path = filedialog.asksaveasfilename(
                        defaultextension=f".{target_format}",
                        filetypes=[("AVI files", "*.avi"), ("All files", "*.*")],
                        title="저장할 파일명 입력"
                    )
                    if file_path:
                        os.rename(target_file, file_path)
                else:
                    os.remove(target_file)

        cv.imshow('Video Player', filtered_img)
        key = cv.waitKey(wait_msec)

        if key == 27:  # ESC
            break
        elif key == ord(' '):
            record = not record
            print(f"Recording: {record}")
        elif key == ord('>') or key == ord('.'):
            filter_mode = (filter_mode + 1) % filter_len
        elif key == ord('<') or key == ord(','):
            filter_mode = (filter_mode - 1) % filter_len

    if target.isOpened():
        target.release()
    video.release()
    cv.destroyAllWindows()
