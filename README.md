# SmartVision-CARLA-YOLOv8 🚗📸

A modular computer vision pipeline built on YOLOv8 and CARLA simulator for autonomous driving perception tasks. This project demonstrates annotation conversion, model training, and deployment-ready structure for international presentation.

## 🔍 Overview

SmartVision-CARLA-YOLOv8 is designed to:
- Convert CARLA simulator annotations to YOLOv8 format
- Train object detection models on synthetic driving data
- Provide a reproducible and modular ML pipeline
- Showcase deployment-ready code for portfolio and migration purposes

## 📁 Project Structure
SmartVision-CARLA-YOLOv8/ ├── data/
# Raw and converted annotations ├── scripts/               
# Conversion, training, and evaluation scripts ├── models/                
# YOLOv8 configs and checkpoints ├── notebooks/             
# Visualization and debugging ├── README.md              
# Project documentation └── requirements.txt       
# Dependencies



## ⚙️ Features

- ✅ Annotation conversion from CARLA to YOLOv8
- ✅ Modular training pipeline with clear configs
- ✅ Debugging tools and visualizations
- ✅ Lightweight setup for rapid prototyping
- ✅ Ready for GitHub presentation and migration portfolios

## 🚀 How to Run
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app/streamlit_demo.py

# Convert annotations
python scripts/convert_annotations.py --input data/carla --output data/yolo

# Train YOLOv8 model
python scripts/train.py --config models/yolov8_config.yaml

🧠 Features of the App
- Upload custom driving images for detection
- View bounding boxes and class predictions in real-time
- Toggle model confidence thresholds
- Lightweight and fast — ideal for showcasing in interviews or portfolios

📸 Sample Results
Include a few sample detection images or metrics here if available.

🌍 Author
Alireza Sobhani
Machine Learning & Computer Vision Developer
Focused on international portfolio building and migration-ready projects.

📫 Contact
Feel free to reach out via LinkedIn or GitHub for collaboration or freelance opportunities.
https://www.linkedin.com/in/alireza-sobhani-385134245
https://wa.me/message/XW6WQJCVM6LQH1

```bash
