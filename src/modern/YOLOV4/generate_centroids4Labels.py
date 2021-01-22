import json

with open('src/modern/YOLOV4/4Labels/output.json', 'r') as f:
    train_dict = json.load(f)

with open('src/modern/YOLOV4/4Labels/output2.json', 'r') as f:
    test_dict = json.load(f)


dicts = []

dicts.append(train_dict)
dicts.append(test_dict)

sizes = {
    "cloudy_width": 640,
    "cloudy_height": 480,
    "cloudy2_width": 640,
    "cloudy2_height": 480,
    "sunny_width": 950,
    "sunny_height": 600,
    "rainy_width": 950,
    "rainy_height": 598,
    "night_width": 1176,
    "night_height": 768
}

# c can be negative or bigger than the width of the image


def check(c, b):
    if c < 0:
        return 0
    elif c > b - 1:
        return b - 1
    else:
        return c


centroids = {}
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

        objects = []
        if len(frame['objects']) != 0:
            for obj in frame['objects']:
                width = sizes[f"{vidName}_width"]
                height = sizes[f"{vidName}_height"]

                class_id = obj["class_id"] + 1
                if class_id == 4:
                    class_id = 2

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

                center_x = int((l+r)/2)
                center_y = int((t+b)/2)

                obj_centroid = str(center_x)+"_" + \
                    str(center_y)+"_"+str(class_id)

                objects.append(obj_centroid)
        centroids[name] = objects

with open('yolo_centroids.json', 'w') as fp:
    json.dump(centroids, fp)
