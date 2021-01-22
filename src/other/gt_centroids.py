import os
import json

clsdict = { "car" : 1, "bike" : 2, "person" : 3 }
path = r"dataset-split-vgg/all/via_region_data.json"
frames = {}

f = open(path)
data = json.load(f)

for d in data:
    name = d["filename"]
    
    for r in d["regions"]:
        
        r = d["regions"][r]

        x1 = r["shape_attributes"]["all_points_x"][0]
        y1 = r["shape_attributes"]["all_points_y"][0]

        x2 = r["shape_attributes"]["all_points_x"][1]
        y2 = r["shape_attributes"]["all_points_y"][2]

        cx = int((x1+x2)/2)
        cy = int((y1+y2)/2)
        c = clsdict[r["region_attributes"]["object_name"]]

        center =  f"{cx}_{cy}_{c}"

        if name in frames:
            frames[name].append(center)
        if name not in frames:
            frames[name] = []
            frames[name].append(center)

with open(r"gt_centroids.json", "w") as f:
  json.dump(frames, fp=f, indent=3)

