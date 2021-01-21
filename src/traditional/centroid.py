import os
import cv2
import json
import numpy as np


frames = {}
car_cascade = cv2.CascadeClassifier('Cascades/cas1.xml')

def cascasde(img, name):

    cars = car_cascade.detectMultiScale(img)
    frames[name] = []

    for (x,y,w,h) in cars:
        
        c1 = int(x + w/2)
        c2 = int(y + h/2)

        frames[name].append(f"{c1}_{c2}_1") 


for name in os.listdir('dataset'):

    for frame in sorted(os.listdir(f'dataset/{name}')):

        files = f'{name}/{frame}'      
        image = cv2.imread('dataset/' + files)
        cascasde(image, f"{name}_{frame}")


with open("haar_centroid.json", "w") as f:
    json.dump(frames, fp=f, indent=3)