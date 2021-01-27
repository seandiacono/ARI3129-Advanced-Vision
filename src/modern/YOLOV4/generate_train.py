import os

image_files = []
os.chdir(os.path.join("dataset-split-yolo", "train"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".png"):
        image_files.append("dataset-split-yolo/train/" + filename)
os.chdir("..")
with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")
