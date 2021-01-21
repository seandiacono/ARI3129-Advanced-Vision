import cv2
import numpy as np
import os

fps = 15
car_cascade = cv2.CascadeClassifier('Cascades/cas1.xml')

def cascasde(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    return img

for name in os.listdir('dataset'):

    img_arr = []

    for frame in sorted(os.listdir(f'dataset/{name}')):

        files = f'{name}/{frame}'      
        image = cv2.imread('dataset/' + files)

        frameH, frameW, _ = image.shape
        size = (frameW, frameH)

        img_arr.append(cascasde(image))


    result = cv2.VideoWriter(name + '.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)       

    for i in range(len(img_arr)):

        result.write(img_arr[i])

    result.release()

