from centroidtracker import CentroidTracker
import numpy as np
import time
import json
import cv2

def get_scale_factor(name):
	return sizes[f"{name}_width"] / dims[name][0], sizes[f"{name}_height"] / dims[name][1]

img_arrays = {"cloudy2" : [], "cloudy": [], "night": [], "rainy": [], "sunny": []}
ct = {"cloudy2" : CentroidTracker(maxDisappeared=10), "cloudy": CentroidTracker(maxDisappeared=10), "night": CentroidTracker(maxDisappeared=10), "rainy": CentroidTracker(maxDisappeared=10), "sunny": CentroidTracker(maxDisappeared=10)}

maskrcnn_pad = {"s1" : 93, "s2" : 133, "s3" : 142}

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

model = "haar"
f = open(f"video-analysis/{model}_centroids.json")
C = json.load(f)
C = dict(sorted(C.items()))
for f in C:

	name = f.split("_")[0]
	frame = cv2.imread(f"dataset/dataset-all/{f}")
	cents = []

	for p in C[f]:
		x, y, c = p.split("_")

		if c == "3":
			continue

		cents.append((int(x), int(y)))

	objects = ct[name].update(cents)

	for (objectID, centroid) in objects.items():

		x = centroid[0]
		y = centroid[1]

		text = "ID {}".format(objectID)

		cv2.putText(frame, text, (x - 10, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
		cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

	img_arrays[name].append(frame)
	
for name in img_arrays:

    img_array = img_arrays[name]
    h, w, _ = img_array[0].shape
    out = cv2.VideoWriter(f"video-analysis/vehicle-tracking/{model}/{name}.avi", cv2.VideoWriter_fourcc(*'DIVX'), 15, (w,h))

    for i in range(len(img_array)):
        img = img_array[i][0:h,0:w]
        out.write(img)

    out.release()