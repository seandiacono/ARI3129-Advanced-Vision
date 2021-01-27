import os
import cv2

fps = 15

img_arrays = {"cloudy2" : [], "cloudy": [], "night": [], "rainy": [], "sunny": []}

model = "haar"

for frame in os.listdir(f"results/{model}-images"):

    name = frame[:-9]

    img = cv2.imread(f"results/{model}-images/{frame}")
        
    height, width, layers = img.shape
    size = (width, height)

    img_arrays[name].append(img)

for name in img_arrays:

    img_array = img_arrays[name]
    h, w, _ = img_array[0].shape
    out = cv2.VideoWriter(f"results/{model}-videos/{name}.avi", cv2.VideoWriter_fourcc(*'DIVX'), fps, (w,h))

    for i in range(len(img_array)):
        img = img_array[i][0:h,0:w]
        out.write(img)

    out.release()