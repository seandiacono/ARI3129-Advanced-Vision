import os
import cv2
from tqdm import tqdm

def saveframe(name, sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    success, image = vidcap.read()
    if success: 
        cv2.imwrite(f"dataset/dataset-scene/{name}/{'%04d' % count}.jpg", image)
    return success

fps = 15
rate = 1/fps

path = r"../videos"

for video in os.listdir(path):

    sec = 0
    count = 1

    vidcap = cv2.VideoCapture(f"{path}/{video}")

    name = video[:-4]
    

    try: os.mkdir(f"dataset/dataset-scene/{name}")
    except FileExistsError: print(f"dataset/dataset-scene/{name} folder already exists")

    success = saveframe(name, sec)

    while success:
        count = count + 1
        sec = sec + rate
        sec = round(sec, 2)
        success = saveframe(name, sec)