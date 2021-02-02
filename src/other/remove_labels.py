import os
import cv2

new_folder = "annotations/annotations-filtered/"
names = ["cloudy", "cloudy2", "night", "rainy", "sunny"]
labels_to_accept = ["0", "1", "2", "3"]

for name in names:
    path = f"annotations/annotations-original/{name}"

    labels = {}

    for file in os.listdir(path):
        raw = open(f"{path}/{file}").read().split("\n")
        
        labels[file[:-4]] = []
        for r in raw:
            r = r.split(" ")

            if r[0] not in labels_to_accept:
                continue
            elif r[0] == "3":
                r[0] = "1"
            
            labels[file[:-4]].append((" ".join(r)))
            
    
        try:
            f = open(f"{new_folder}/{name}/{file}", 'w')
        except:
            os.mkdir(f"{new_folder}/{name}")
            f = open(f"{new_folder}/{name}/{file}", 'w')

        for label in labels[file[:-4]]:
            f.write("%s\n" % label)