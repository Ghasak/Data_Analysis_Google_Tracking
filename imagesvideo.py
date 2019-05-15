import cv2
import os

SAVE_DIR = "word_images_1yrwin_1dslide"

# windows:
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
# Linux:
#fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
# MAC:
# fps = 15
# capSize = (800, 450)  # this is the size of my source video
# fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')  # note the lower case
# self.vout = cv2.VideoWriter()
# success = self.vout.open('output.mov', fourcc, fps, capSize, True)
# https://stackoverflow.com/questions/10605163/opencv-videowriter-under-osx-producing-no-output
# https://stackoverflow.com/questions/26452909/opencv-write-frame-to-file-python
# fourcc = cv2.CV_FOURCC('m', 'p', '4', 'v')  # This one for the MAC
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')


out = cv2.VideoWriter(f"./{SAVE_DIR}/video.avi", fourcc, 60.0, (1200, 700))

for i in range(3311):  # The range of all images we have created which is about [3311]
    img_path = f"./{SAVE_DIR}/{i}.png"
    print(f"./{SAVE_DIR}/{i}.png")
    frame = cv2.imread(img_path)
    out.write(frame)

out.release()
