import os
import random
import cv2

img_root = r"dataset/dataset-all"

def write_anns(sub, mode):
    for img in sub:
        name = img[:-9]
        number = img[len(name)+1:-4]

        toread = f"annotations//annotations-filtered//{name}//{number}.txt"
        folder = open(toread).read()

        with open(f"../{mode}/{name}_{number}.txt", "w+") as f:
            f.write(folder)

def write_images(sub, mode):
    for img in sub:

        name = img[:-9]
        number = img[len(name)+1:-4]

        toread = f"dataset//dataset-all//{name}_{number}.jpg"

        image = cv2.imread(toread)

        cv2.imwrite(f"../{mode}/{name}_{number}.jpg", image)


# get all image paths and split them training and validation
img_list = os.listdir(img_root)
random.shuffle(img_list)  
t = int(len(img_list) * 0.9)
train = img_list[:t]
val = img_list[t:]

# write the absolute path of each image in the respective folder
write_anns(train, mode="train")
write_anns(val, mode="val")

# save images in same folder as above
write_images(train, mode="train")
write_images(val, mode="val")
