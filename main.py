import cv2
import os

video_path = 'video/true/5.mp4'
save_path = 'image/true'

cap = cv2.VideoCapture(video_path)

l = os.listdir(save_path)
if l != []:
    l = [int(i.split('.')[0]) for i in l]
    l.sort()
    frame_index = l[-1] + 1
else:
    frame_index = 0

last_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT) + frame_index
if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(os.path.join(save_path, '%d.jpg' %
                        frame_index), frame)
            frame_index += 1
            print('frame: %d/%d' % (frame_index, last_frame))
        else:
            break
else:
    print("can't open video.")

cap.release()
