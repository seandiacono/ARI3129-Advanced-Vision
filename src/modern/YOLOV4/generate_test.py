import os

image_files = []
os.chdir(os.path.join("dataset-split-yolo", "test"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".png"):
        image_files.append("dataset-split-yolo/test/" + filename)
os.chdir("..")
with open("test.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")