import numpy as np
import cv2
import time

video = cv2.VideoCapture("dataset/dataset-videos/night.mp4")

# Takes the first 30 frames for background estimation
FOI = video.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=30)

# Takes the frames and adds them to a list
frames = []
for frameOI in FOI:
    video.set(cv2.CAP_PROP_POS_FRAMES, frameOI)
    ret, frame = video.read()
    frames.append(frame)

# Taking median pixel values to get a background image
bgFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
cv2.imshow('bg', bgFrame)
cv2.waitKey(0)

while True:
    ret, frame = video.read()

    if frame is None:
        print('error reading video')
        break

    # Subtracting in both directions and then adding the different thresholds together to create a better mask
    subtraction1 = cv2.subtract(bgFrame, frame)
    subtraction2 = cv2.subtract(frame, bgFrame)

    gray1 = cv2.cvtColor(subtraction1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(subtraction2, cv2.COLOR_BGR2GRAY)

    ret, fgmask1 = cv2.threshold(gray1, 15, 255, cv2.THRESH_BINARY)
    ret, fgmask2 = cv2.threshold(gray2, 15, 255, cv2.THRESH_BINARY)

    fgmask = cv2.add(fgmask1, fgmask2)

    # Morphological operations to remove noise and close gaps
    kernel = np.ones((5, 5), np.uint8)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel, iterations=1)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel, iterations=2)
    fgmask = cv2.dilate(fgmask, kernel, iterations=3)

    # Extracting foreground
    fg = cv2.bitwise_and(frame, frame, mask=fgmask)

    cv2.imshow('Video', frame)
    cv2.imshow('fgmask', fgmask)
    cv2.imshow('gray1', gray1)
    cv2.imshow('gray2', gray2)
    cv2.imshow('fg', fg)

    time.sleep(0.1)
    k = cv2.waitKey(1)
    if k == 'q':
        break

video.release()
cv2.destroyAllWindows()
