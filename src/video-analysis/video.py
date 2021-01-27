import os
import cv2
import json
import numpy as np 

font = cv2.FONT_HERSHEY_SIMPLEX
model = r"haar"
path = f"results/{model}-images"
count = json.load(open(f"video-analysis-results/lane-count/{model}_count.json"))
polys = {}
maskrcnn_pad = {"s1" : 93, "s2" : 133, "s3" : 142}

red = (0, 0, 255)
blue = (255, 0, 0)

sizes = {
    "s1_width" : 640,
    "s1_height" : 480,
    "s2_width" : 950,
    "s2_height" : 600,
    "s3_width" : 1176,
    "s3_height" : 768
}

dims = {
    "s1" : (797, 640),
    "s2" : (797, 559),
    "s3" : (797, 536)
}

S = {"cloudy" : "s1", "cloudy2" : "s1", "rainy" : "s2", "sunny" : "s2", "night" : "s3"}
img_arrays = {"cloudy2" : [], "cloudy": [], "night": [], "rainy": [], "sunny": []}

def get_scale_factor(name):
  name = name.split("_")[0]
  return sizes[f"{name}_width"] / dims[name][0], sizes[f"{name}_height"] / dims[name][1]

def draw_polygon(img, poly, colour):
    pts = np.array(poly, np.int32)
    pts = pts.reshape((-1,1,2))
    return cv2.polylines(img, [pts], True, colour)

def write_text(img, name, count, sx, sy, c):
    cv2.putText(img, f"{name} lane", (sx, sy), font, 1, c, 2, cv2.LINE_AA)
    cv2.putText(img, f"Cars: {count[0]}", (sx, sy+30), font, 0.75, c, 2, cv2.LINE_AA)
    cv2.putText(img, f"Bikes: {count[1]}", (sx, sy+60), font, 0.75, c, 2, cv2.LINE_AA)
    cv2.putText(img, f"Persons: {count[2]}", (sx, sy+90), font, 0.75, c, 2, cv2.LINE_AA)


for file in os.listdir(r"video-analysis-results/lane-count/parts"):
    name = file.split(".")[0]
    j = json.load(open(f"video-analysis-results/lane-count/parts/{file}"))

    sx, sy = (1, 1)
    c = 0

    if model == "maskrcnn":
        sx, sy = get_scale_factor(name)
        c = maskrcnn_pad[name]

    polys[f"{name}_left"] = [(int(x / sx), int(y / sy) + c) for (x,y) in j["left"]]
    polys[f"{name}_right"] = [(int(x / sx), int(y / sy)  + c) for (x,y) in j["right"]]

for file in os.listdir(path):

    name = file.split("_")[0]

    left = count[f"{file}_left"]
    right = count[f"{file}_right"]

    img = cv2.imread(f"{path}/{file}")

    img = draw_polygon(img, polys[f"{S[name]}_left"], blue)
    img = draw_polygon(img, polys[f"{S[name]}_right"], red)

    write_text(img, "Left", left, sx=10, sy=50, c=blue)
    write_text(img, "Right", right, sx=img.shape[0], sy=50, c=red)

    img_arrays[name].append(img)

for name in img_arrays:

    img_array = img_arrays[name]
    h, w, _ = img_array[0].shape
    out = cv2.VideoWriter(f"video-analysis-results/lane-count/{model}/{name}.avi", cv2.VideoWriter_fourcc(*'DIVX'), 15, (w,h))

    for i in range(len(img_array)):
        img = img_array[i][0:h,0:w]
        out.write(img)

    out.release()