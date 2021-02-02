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

    with open(f"dataset/dataset-split-yolo/test/{frame}.txt", 'r') as f:
        
        file = f.read()
        gt = file.split("\n")
        
        height, width, _ = img.shape
        gt = convert(gt, height, width)
    return gt

def get_pred(img):
    
    pred = []
    rectangles, confidence = car_cascade.detectMultiScale2(img, scaleFactor=1.3, minNeighbors=5)

    for i,(x,y,w,h) in enumerate(rectangles):
        pred.append([x,y, x+w, y+h, 0, confidence[i][0]])

    return np.array(pred)

metric_fn = MeanAveragePrecision(num_classes=1)
car_cascade = cv2.CascadeClassifier('src/traditional/car.xml')

for frame in os.listdir('dataset/dataset-split-yolo/test/'):

    if frame.endswith('.txt'):
        continue

    frame = frame[:-4]
    img = cv2.imread(f"dataset/dataset-split-yolo/test/{frame}.jpg")

    preds = get_pred(img)
    gt = get_gt(frame, img)

    try:
        metric_fn.add(preds, gt)
    except:
        continue

# compute metric COCO metric
print(f"COCO mAP: {metric_fn.value(mpolicy='soft')['mAP']}")

