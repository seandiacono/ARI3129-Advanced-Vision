import os
import cv2

new_folder = "new_annotations"
names = ["cloudy", "cloudy2", "night", "rainy", "sunny"]
labels_to_accept = ["0", "1", "2", "3"]

for name in names:
    path = f"annotations/{name}"

    labels = {}

    for file in os.listdir(path):
        raw = open(f"{path}/{file}").read().split("\n")
        
        labels[file[:-4]] = [r.replace("3", "1") for r in raw if r.split(" ")[0] in labels_to_accept]

        try:
            f = open(f"{new_folder}/{name}/{file}", 'w')
        except:
            os.mkdir(f"{new_folder}/{name}")
            f = open(f"{new_folder}/{name}/{file}", 'w')

        for label in labels[file[:-4]]:
            f.write("%s\n" % label)