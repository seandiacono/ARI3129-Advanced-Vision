import os
import cv2
import json

color = {1: (0, 0, 255), 2: (255, 0, 0), 3: (0, 255, 0)}
classes = {1: 'car', 2: 'bike', 3: 'person'}


def draw(img, objs):
    img = img.copy()
    height, width, _ = img.shape

    for obj in frame['objects']:

        class_id = obj["class_id"] + 1
        if class_id == 4:
            class_id = 2

        confidence = round(obj["confidence"] * 100, 1)

        x = obj["relative_coordinates"]["center_x"]
        y = obj["relative_coordinates"]["center_y"]
        w = obj["relative_coordinates"]["width"]
        h = obj["relative_coordinates"]["height"]

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

        cv2.rectangle(img, (l, t), (r, b), color[class_id], thickness=2)
        cv2.putText(img, classes[class_id] + " " + str(confidence) + "%", (l, t-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,  color[class_id], 2)

    return img


with open('src/modern/YOLOV4/4Labels/output.json', 'r') as f:
    train_dict = json.load(f)

with open('src/modern/YOLOV4/4Labels/output2.json', 'r') as f:
    test_dict = json.load(f)

dicts = []

dicts.append(train_dict)
dicts.append(test_dict)

for dictionary in dicts:
    for frame in dictionary:
        name = frame["filename"].split("/")[2]

        parts = name.split("_")
        frameNo = parts[0]
        vidName = parts[1].split(".")[0]

        if vidName == "cloudy1":
            vidName = "cloudy"
        elif vidName == "rain":
            vidName = "rainy"

        name = vidName + "_" + frameNo + ".jpg"

        path = f"dataset/{name}"
        img = cv2.imread(path)
        objs = frame["objects"]

        if img is None:
            print(name)
        else:
            img = draw(img, objs)
            cv2.imwrite(f"datasetYOLOBoxes/{name}", img)


# for name in names:

#     path = f"dataset/{name}"

#     img_array = []

#     for frame in os.listdir(path):

#         img = cv2.imread(f"{path}/{frame}")
#         img = draw(img, labels[frame[:-4]])

#         img_array.append(img)

#     height, width, _ = img_array[0].shape
#     size = (width, height)

#     fps = 15
#     out = cv2.VideoWriter(
#         f'{name}.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

#     for i in range(len(img_array)):
#         out.write(img_array[i])
#     out.release()
