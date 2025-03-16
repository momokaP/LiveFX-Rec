# LiveFX-Rec

### 소개
LiveFX Rec는 python으로 개발한 실시간으로 웹 캠 영상을 확인하면서 다양한 필터 효과를 적용하여 녹화할 수 있는 프로그램입니다. 

OpenCV 기반의 필터 효과를 통해 사용자는 영상을 촬영하면서 필터 효과를 적용할 수 있습니다. 

녹화 중 필터 효과를 변경할 수 있으며, 녹화 종료 후에는 영상을 저장하거나 삭제할 수 있도록 선택할 수 있습니다. 

### 프로그램 시연 사진-영상
##### 사진
![101](https://github.com/user-attachments/assets/7a1a9ad3-58ce-46cd-abe9-efd2ddc8e5d6)
**Preview**
![102](https://github.com/user-attachments/assets/6ef79ed9-f3c6-495a-92d3-73084d617222)
**Record**
![103](https://github.com/user-attachments/assets/8b6d04e4-3aa2-4210-8333-d3dbf0ce15bd)
![104](https://github.com/user-attachments/assets/b61cb9bf-b029-466f-9a7d-d50f4baaf69f)
**File Save**

##### 영상
https://github.com/user-attachments/assets/13c5ab61-0ac4-4001-87ec-808919938d8d
**프로그램으로 녹화**

**녹화 결과물**



### 주요 기능
- 실시간 웹캠 미리보기: 녹화 전에 영상을 실시간으로 확인 가능
- 다양한 필터 효과: '<' '>' 키를 통해 OpenCV 기반의 영상 필터 적용
- 간편한 녹화 시작/중지: 'Space' 키를 통해 녹화 컨트롤
- 파일 저장 여부 선택: 녹화 종료 후 저장 여부를 선택할 수 있음
- 사용자 지정 파일 저장: 원하는 파일명과 위치에 영상 저장 가능

### 사용 방법
- 프로그램 실행 후 웹캠 화면을 확인합니다.
- 'Space' 키를 눌러 녹화를 시작/중지합니다.
- 녹화 중에는 '<' '>' 키를 통해 적용할 필터를 변경할 수 있습니다.
- 녹화 종료 후 저장 여부를 선택합니다.
- 저장할 경우 원하는 파일명을 입력하여 저장합니다.

### 사용한 라이브러리
- cv2
- tkinter
- os
