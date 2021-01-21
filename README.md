Directory of project

```
ARI3129-Advanced-Vision
├── annotations
├── annotations-filtered
├── dataset
├── dataset-scene
├── dataset-split-vgg
├── dataset-split-yolo
├── maskrcnn-images
├── maskrcnn-videos
├── road-count
└── src
    ├── modern
    ├── other
    ├── road-count
    └── traditional
```

| Folder      | Description | Found in repository | Task/s
| ------------ | ----------- | --- | - |
| annotations   | Annotations obtained from the EVA tool (in YOLO format)      | | 2
| annotations-filtered   | Filtered annotations, removing empty frames and contains less labels | ☑ | 2
| dataset   | Contains all images    | ☑ | 1
| dataset-scene   | Contains all images, split by scene in separate folders        | | 1
| dataset-split-vgg   | Splits images in training (80%), validation (10%), testing (10%) and all (100%) for MaskRCNN model. Also contains annotations in VGG format.    | | 4
| dataset-split-yolo   | Splits images in training (80%) and testing (20%) for YOLOv4 model. Also contains annotations in YOLO format.  | | 3
| maskrcnn-images   | Contains all images, showing detected objects by the MaskRCNN model        | | 3
| maskrcnn-videos   | _maskrcnn-images_ in video format     | | 3
| road-count   | Video analysis deliverables       | | 5
| src  | Contains Python scripts    | ☑ | 2-5