from centroidtracker import CentroidTracker
import numpy as np
import time
import json
import cv2


img_arrays = {"cloudy2" : [], "cloudy": [], "night": [], "rainy": [], "sunny": []}
ct = {"cloudy2" : CentroidTracker(maxDisappeared=10), "cloudy": CentroidTracker(maxDisappeared=10), "night": CentroidTracker(maxDisappeared=10), "rainy": CentroidTracker(maxDisappeared=10), "sunny": CentroidTracker(maxDisappeared=10)}

model = "haar"
f = open(f"video-analysis-results/{model}_centroids.json")
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
    out = cv2.VideoWriter(f"video-analysis-results/vehicle-tracking/{model}/{name}.avi", cv2.VideoWriter_fourcc(*'DIVX'), 15, (w,h))

    for i in range(len(img_array)):
        img = img_array[i][0:h,0:w]
        out.write(img)

    out.release()