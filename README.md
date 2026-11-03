# Intelligent Traffic Surveillance and Automated E-Challan System

## Project Overview
This project aims to develop an intelligent traffic surveillance system that detects traffic violations using video footage.

The current development focuses on detecting and tracking vehicles in traffic videos using YOLO and OpenCV. The next stage is to identify wrong-side driving by analysing vehicle movement and direction.

## Current Progress
- Vehicle detection using YOLOv8.
- Vehicle tracking with unique IDs.
- Bounding boxes around detected vehicles.
- Processing and saving annotated traffic videos.
- Initial testing with traffic video footage.

## Technologies Used
- Python
- OpenCV
- YOLOv8 (Ultralytics)
- NumPy
- Visual Studio Code

## Project Structure
```text
Wrong_Side_Detection/
│
├── main.py
├── inspect_video.py
├── videos/
├── output/
└── .gitignore
```

## Upcoming Features
- Wrong-side driving detection.
- Vehicle movement and direction analysis.
- Verification of suspected traffic violations.
- Evidence generation for detected violations.
- Automated e-challan generation with human review.

## Objective
To improve traffic monitoring by detecting wrong-side driving and supporting more accurate identification of traffic violations through computer vision.
