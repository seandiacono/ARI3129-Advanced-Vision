
#? [{
#?     "filename": "000dfce9-f14c-4a25-89b6-226316f557f3.jpeg",
#?     "regions": {
#?         "0": {
#?             "region_attributes": {
#?                 "object_name": "Cat"
#?             },
#?             "shape_attributes": {
#?                 "all_points_x": [75.30864197530865, 80.0925925925926, 80.0925925925926, 75.30864197530865],
#?                 "all_points_y": [11.672189112257607, 11.672189112257607, 17.72093488703078, 17.72093488703078],
#?                 "name": "polygon"
#?             }
#?         },
#?         "1": {
#?             "region_attributes": {
#?                 "object_name": "Cat"
#?             },
#?             "shape_attributes": {
#?                 "all_points_x": [80.40123456790124, 84.64506172839506, 84.64506172839506, 80.40123456790124],
#?                 "all_points_y": [8.114103362391036, 8.114103362391036, 12.205901974737595, 12.205901974737595],
#?                 "name": "polygon"
#?             }
#?         }
#?     },
#?     "width": 504,
#?     "height": 495
#? }]

import os
import cv2
import json
import random

annPath = "new_annotations"
names = ["cloudy", "cloudy2", "sunny", "rainy", "night"]
sizes = {
    "cloudy_width" : 640,
    "cloudy_height" : 480,
    "cloudy2_width" : 640,
    "cloudy2_height" : 480,
    "sunny_width" : 950,
    "sunny_height" : 600,
    "rainy_width" : 950,
    "rainy_height" : 598,
    "night_width" : 1176,
    "night_height" : 768
    }
classes = {0: "car", 1: "bike", 2: "person"}
vgg_labels = []
vgg_path = "vgg_dataset"

def save_labels(labels, mode):
    images = []

    for label in labels:
        images.append(label["filename"])

    for imgName in images:
        img = cv2.imread(f"images/{imgName}")
        cv2.imwrite(f"{vgg_path}/{mode}/{imgName}", img)

    with open(f"{vgg_path}/{mode}/via_region_data.json", "w") as f:
        json.dump(labels, f)   

def split(L, t):
    random.shuffle(L)  
    a = L[:t]
    b = L[t:]
    return a, b

# c can be negative or bigger than the width of the image
def check(c, b):
    if c < 0: return 0
    elif c > b - 1: return b - 1
    else: return c

def convert2vgg(name, yolo):
    width = sizes[f"{name[:-5]}_width"]
    height = sizes[f"{name[:-5]}_height"]

    vgg = {}

    vgg["filename"] = name + ".jpg"

    vgg["regions"] = {}

    for i, label in enumerate(yolo):

        if label == '': continue
        c, x, y, w, h = map(float, label.split(' '))
        i = str(i)

        vgg["regions"][i] = {}

        vgg["regions"][i]["region_attributes"] = {}
        vgg["regions"][i]["region_attributes"]["object_name"] = classes[int(c)]

        vgg["regions"][i]["shape_attributes"] = {}

        x1 = int((x - w / 2) * width)
        x2 = int((x + w / 2) * width)
        y1 = int((y - h / 2) * height)
        y2 = int((y + h / 2) * height)

        x1 = check(x1, width)
        x2 = check(x2, width)
        y1 = check(y1, height)
        y2 = check(y2, height)
        
        vgg["regions"][str(i)]["shape_attributes"]["all_points_x"] = [x1, x2, x2, x1]
        vgg["regions"][str(i)]["shape_attributes"]["all_points_y"] = [y1, y1, y2, y2]
        vgg["regions"][str(i)]["shape_attributes"]["name"] = "polygon"

        vgg["width"] = width
        vgg["height"] = height

    return vgg

for name in names:
    for file in os.listdir(f"{annPath}/{name}"):
        number = file[:-4]
        yolo = open(f"{annPath}/{name}/{file}").read().split("\n")
        vgg = convert2vgg(name = f"{name}_{number}", yolo=yolo)
        vgg_labels.append(vgg)

#all_labels = vgg_labels

#train_labels, other_labels = split(all_labels, int(len(all_labels) * 0.8))
#val_labels, test_labels = split(other_labels, int(len(other_labels) * 0.5))

#save_labels(train_labels, mode="train")
#save_labels(val_labels, mode="val")
#save_labels(test_labels, mode="test")
#save_labels(all_labels, mode="all")