import json

with open('src/modern/YOLOV4/output.json', 'r') as f:
    train_dict = json.load(f)

with open('src/modern/YOLOV4/output2.json', 'r') as f:
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
        vidName = name.split("_")[0]
        objects = []
        if len(frame['objects']) != 0:
            for obj in frame['objects']:
                width = sizes[f"{vidName}_width"]
                height = sizes[f"{vidName}_height"]

                class_id = obj["class_id"] + 1

                x = obj["relative_coordinates"]["center_x"]
                y = obj["relative_coordinates"]["center_y"]
                w = obj["relative_coordinates"]["width"]
                h = obj["relative_coordinates"]["height"]

                new_x = int((x-w) * width)
                new_y = int((y-h) * height)

                new_x = check(new_x, width)
                new_y = check(new_y, height)

                obj_centroid = str(new_x)+"_"+str(new_y)+"_"+str(class_id)

                objects.append(obj_centroid)
        centroids[name] = objects

with open('yolo_centroids.json', 'w') as fp:
    json.dump(centroids, fp)
