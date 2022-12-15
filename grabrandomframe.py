import cv2
import random
video_path = 'D:\Videorecordings\pando4.mp4'


for number in range(0, 10):
    vidcap = cv2.VideoCapture(video_path)
# get total number of frames
    totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    randomFrameNumber = random.randint(0, totalFrames)
# set frame position
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, randomFrameNumber)
    success, image = vidcap.read()
    if success:
        cv2.imwrite(f"random_frame{number}.jpg", image)
