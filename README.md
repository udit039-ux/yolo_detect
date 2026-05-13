# YOLO Detect

A Python-based object detection project using YOLOv8 for real-time detection via camera feed or video files.

## Project Structure

- **camera_indexing.py** - Script for indexing and identifying available cameras
- **yolo_detect.py** - Main detection script using YOLOv8
- **my_model.pt** - Trained YOLOv8 model weights
- **train/** - Training directory containing:
  - `args.yaml` - Training configuration
  - `results.csv` - Training metrics and results
  - `weights/` - Model weights (best.pt, last.pt)
- **runs/detect/** - Detection prediction results organized by prediction run

## Installation

1. Clone this repository
2. Install required dependencies (YOLOv8, OpenCV, etc.)
3. Ensure you have a conda environment set up (see `How_to_operate(conda_yolo).txt`)

## Usage

### Run Detection
```bash
python yolo_detect.py
```

### Camera Indexing
```bash
python camera_indexing.py
```

## Model

- Uses a pre-trained YOLOv8 model (`my_model.pt`)
- Can be fine-tuned using the training configuration in `train/args.yaml`

## Requirements

- Python 3.8+
- ultralytics
- opencv-python
- torch
- torchvision

## License

MIT License
