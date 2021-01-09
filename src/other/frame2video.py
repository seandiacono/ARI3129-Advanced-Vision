import os
import cv2

fps = 15

for name in os.listdir("../videos"):

    name = name[:-4]

    img_array = []

    for frame in os.listdir(f"dataset/{name}"):

        img = cv2.imread(f"dataset/{name}/{frame}")
        
        height, width, layers = img.shape
        size = (width, height)

        img_array.append(img)

    out = cv2.VideoWriter(f"dataset/{name}.avi", cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()