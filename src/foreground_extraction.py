import numpy as np
import cv2

video = cv2.VideoCapture(
    'C:/Users/seand/OneDrive/Documents/University/Advanced Vision/ARI3129-Advanced-Vision/videos/Video 3.mp4')

fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=False)


while True:
    ret, frame = video.read()

    if frame is None:
        print('error reading video')
        break

    fgmask = fgbg.apply(frame)
    fg = cv2.bitwise_and(frame, frame, mask=fgmask)

    cv2.imshow('Video', frame)
    cv2.imshow('mask', fgmask)
    cv2.imshow('fg', fg)

    k = cv2.waitKey(0)
    if k == 'q':
        break

video.release()
cv2.destroyAllWindows()
