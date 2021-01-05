import os
import cv2

color = {0: (0, 0, 255), 1: (255, 0, 0), 2: (0, 255, 0), 3: (0, 0, 0), 4: (255, 255, 0), 5: (255, 0, 255), 6: (255, 255, 255)}

def draw(img, labels):
    img = img.copy()
    height, width, _ = img.shape

    for label in labels:

        if label == '':
            continue

        c, x, y, w, h = map(float, label.split(' '))

        l = int((x - w / 2) * width)
        r = int((x + w / 2) * width)
        t = int((y - h / 2) * height)
        b = int((y + h / 2) * height)
        
        if l < 0:
            l = 0
        if r > width - 1:
            r = width - 1
        if t < 0:
            t = 0
        if b > height - 1:
            b = height - 1

        cv2.rectangle(img, (l, t), (r, b), color[int(c)], 1)

    return img

name = "sunny"

path = f"dataset/{name}"

# load annotations
ann = f"annotations/{name}"
labels = {}

for file in os.listdir(ann):
    labels[file[:-4]] = open(f"{ann}/{file}").read().split("\n")

img_array = []

for frame in os.listdir(path):
    img = cv2.imread(f"{path}/{frame}")
    img = draw(img, labels[frame[:-4]])

    img_array.append(img)

height, width, _ = img_array[0].shape
size = (width, height)

fps = 15
out = cv2.VideoWriter(f'{name}.avi',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()