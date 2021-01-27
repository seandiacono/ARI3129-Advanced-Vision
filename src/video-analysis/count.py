import os
import json
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
#? s1 : cloudy / cloudy2
#? s2 : rainy / sunny
#? s3 : night

S = {"cloudy" : "s1", "cloudy2" : "s1", "rainy" : "s2", "sunny" : "s2", "night" : "s3"}
classes = {"car" : 0, "bike" : 1, "person" : 2}

model = "haar"
path = f"video-analysis-results/lane-count/parts"
scenes = {}
counter = {}

for file in os.listdir(path):
    name = file.split(".")[0]
    j = json.load(open(f"{path}/{file}"))
    scenes[f"{name}_left"] = Polygon([(int(x), int(y)) for (x,y) in j["left"]])
    scenes[f"{name}_right"] = Polygon([(int(x), int(y)) for (x,y) in j["right"]])

f = open(f"video-analysis-results/{model}_centroids.json")
C = json.load(f)

for f in C:

    scene = S[f.split("_")[0]]

    counter[f"{f}_left"] = [0, 0, 0]
    counter[f"{f}_right"] = [0, 0, 0]

    for p in C[f]:

        x, y, c = p.split("_")
        pt = Point(int(x),int(y))

        if scenes[f"{scene}_left"].contains(pt):
            counter[f"{f}_left"][int(c)-1] += 1
        elif scenes[f"{scene}_right"].contains(pt):
            counter[f"{f}_right"][int(c)-1] += 1

with open(f"{model}_count.json", "w") as f:
  json.dump(counter, fp=f, indent=3)
