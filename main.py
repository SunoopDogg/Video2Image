import cv2
import os

# mp4 파일 경로
video_path = 'video/true/1.mp4'

# 이미지 저장 경로
save_path = 'image/true'

# mp4 파일 읽기
cap = cv2.VideoCapture(video_path)

if os.listdir(save_path) != []:
    frame_index = int(os.listdir(save_path)[-1].split('.')[0]) + 1
else:
    frame_index = 0

# 이미지 추출
if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(os.path.join(save_path, '%d.jpg' %
                        frame_index), frame)
            frame_index += 1
        else:
            break
else:
    print("can't open video.")

cap.release()
