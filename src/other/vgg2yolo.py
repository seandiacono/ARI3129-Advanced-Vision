import os
import cv2

def write_ann(frame, folder):
    name = frame.split("_")[0]
    number = frame.split("_")[1].split(".")[0]
    anns = open(f"new_annotations/{name}/{number}.txt").read().split("\n")

    f = open(f"{yolo}/{folder}/{name}_{number}.txt", 'w+')

    for ann in anns:
        f.write("%s\n" % ann)

    f.close()

vgg = "vgg_dataset"
yolo = "yolo_dataset"
folders = ["test", "train", "val"]

for folder in folders:

    frames = os.listdir(f"{vgg}/{folder}")

    for frame in frames:
        if frame.endswith(".jpg"):
            write_ann(frame, folder)
            cv2.imwrite(f"{yolo}/{folder}/{frame}", cv2.imread(f"{vgg}/{folder}/{frame}"))
            

            
        