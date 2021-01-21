from mean_average_precision import MeanAveragePrecision
import cv2
import numpy as np
import os


def check(c, b):
    if c < 0: return 0
    elif c > b - 1: return b - 1
    else: return c

def convert(g, height, width):

    gt = []

    for label in g:
        if label == '':
            continue

        c, x, y, w, h = map(float, label.split(' '))    
        
        if c != 0.0:
            continue

        x1 = int((x - w / 2) * width)
        x2 = int((x + w / 2) * width)
        y1 = int((y - h / 2) * height)
        y2 = int((y + h / 2) * height)

        x1 = check(x1, width)
        x2 = check(x2, width)
        y1 = check(y1, height)
        y2 = check(y2, height)

        gt.append([x1,y1,x2,y2,c,0,0])

    return np.array(gt)

def get_gt(frame, img):
    gt = []

    with open(f"test/{frame}.txt", 'r') as f:
        
        file = f.read()
        gt = file.split("\n")
        
        height, width, _ = img.shape
        gt = convert(gt, height, width)
    return gt

def get_pred(img):
    
    pred = []
    rectangles, confidence = car_cascade.detectMultiScale2(img)

    for i,(x,y,w,h) in enumerate(rectangles):
        pred.append([x,y, x+w, y+h, 0, confidence[i][0]])

    return np.array(pred)

# create metric_fn
metric_fn = MeanAveragePrecision(num_classes=1)
car_cascade = cv2.CascadeClassifier('Cascades/cas1.xml')

for frame in os.listdir('test'):

    if frame.endswith('.txt'):
        continue

    frame = frame[:-4]
    img = cv2.imread(f"test/{frame}.jpg")

    preds = get_pred(img)
    gt = get_gt(frame, img)
    metric_fn.add(preds, gt)


# compute PASCAL VOC metric
print(f"VOC PASCAL mAP: {metric_fn.value(iou_thresholds=0.5, recall_thresholds=np.arange(0., 1.1, 0.1))['mAP']}")

# compute PASCAL VOC metric at the all points
print(f"VOC PASCAL mAP in all points: {metric_fn.value(iou_thresholds=0.5)['mAP']}")

# compute metric COCO metric
print(f"COCO mAP: {metric_fn.value(iou_thresholds=np.arange(0.5, 1.0, 0.05), recall_thresholds=np.arange(0., 1.01, 0.01), mpolicy='soft')['mAP']}")

