from sklearn.metrics import mean_squared_error
import os
import json

model = "haar"
s = "cloudy"
true_path = f"video-analysis/lane-count/gt_count.json"
pred_path = f"video-analysis/lane-count/{model}_count.json"

y_true_d = dict(sorted(json.load(open(true_path)).items()))
y_pred_d = dict(sorted(json.load(open(pred_path)).items()))

for k in list(y_true_d.keys()):
    if not  k.startswith(s):
        del y_true_d[k]

for k in list(y_pred_d.keys()):
    if not k.startswith(s):
        del y_pred_d[k]

#!print(set(y_pred_d) - set(y_true_d))

y_true = list(y_true_d.values())
y_pred = list(y_pred_d.values())

print(mean_squared_error(y_true, y_pred))