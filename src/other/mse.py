from sklearn.metrics import mean_squared_error
import os
import json

model = "maskrcnn"
true_path = f"road-count/gt_count.json"
pred_path = f"road-count/{model}_count.json"

y_true_d = json.load(open(true_path))
y_pred_d = json.load(open(pred_path))

#! print(sorted(set(y_pred_d)-set(y_true_d)))

y_true = list(y_true_d.values())
y_pred = list(y_pred_d.values())

print(mean_squared_error(y_true, y_pred))