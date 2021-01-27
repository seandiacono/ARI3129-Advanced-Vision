Please download release for executable samples._

Directory of project is found below. 

```
ARI3129-Advanced-Vision
├── annotations
    ├── annotations-filtered
    └── annotations-original
├── dataset
    ├── dataset-all
    ├── dataset-scene
    ├── dataset-split-vgg
    ├── dataset-split-yolo
    └── dataset-videos
├── eva
├── results
├── src
    ├── modern 
    ├── other 
    ├── traditional 
    └── video-analysis
└── video-analysis-results
    ├── lane-count
    └── vehicle-tracking
```

Folders not included in repository can be downloaded from: https://drive.google.com/file/d/1eN8hARLyn6STg5dQm4c07ud3A46V71V1/view?usp=sharing (only accessible to University of Malta account holders)

| Folder      | Description | Task/s | Found in repository
| ------------ | ----------- | --- | - |
| annotations-filtered   | Filtered annotations, removing empty frames and with annotation mode $A_3$. | 2 | ☑
| annotations-original   | Raw annotations in YOLO format, obtained from EVA tool. | 2 | 
| dataset-all   | Contains all images    | 1 | ☑
| dataset-scene   | Contains all images, split by scene in separate folders.        | 1 | 
| dataset-split-vgg   | Splits images in training (80%), validation (10%), testing (10%) and all (100%) for MaskRCNN model. Also contains annotations in VGG format.    | 4 |
| dataset-split-yolo   | Splits images in training (80%) and testing (20%) for YOLOv4 model. Also contains annotations in YOLO format.  | 3 |
| eva  | EVA annotation tool.  | 2 | ☑
| results   | Contains all images and videos, showing detected objects by the YOLOv4, Mask R-CNN and Haar cascade models.   | 3-4 |
| src  | Contains the Python scripts.   | 2-5 | ☑
| video-analysis-results   | Contains Task 5 results, including car counting by lanes and object tracking.   | 5 |