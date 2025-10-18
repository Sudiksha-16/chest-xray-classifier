# chest-xray-classifier

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Next.js](https://img.shields.io/badge/Next.js-15-black)](https://nextjs.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Overview
**chest-xray-classifier** is a fully custom Convolutional Neural Network (CNN) built from scratch using NumPy. It classifies chest X-ray images into normal or pneumonia cases, demonstrating deep learning fundamentals without relying on high-level frameworks like TensorFlow or PyTorch.

---

## Tech Stack

### Frontend
- **Framework**: Next.js 15 (App Router)  
- **Language**: JavaScript/JSX  
- **Styling**: Tailwind CSS v4  
- **State Management**: React Hooks (`useState`, `useEffect`)  
- **UI Components**: shadcn/ui  

### Backend
- **Runtime**: Node.js  
- **Framework**: Next.js API Routes  
- **Language**: JavaScript  

### Machine Learning
- **Language**: Python  
- **Core Library**: NumPy  
- **Architecture**: Custom CNN from scratch  
- **Model Persistence**: Pickle (.pkl)

---

## Features
- Load and preprocess chest X-ray images  
- Custom CNN with convolution, pooling, flatten, dense, and softmax layers  
- Train model from scratch without external ML libraries  
- Save and load trained model as `.pkl` file  
- End-to-end web interface for real-time classification  

---

## Dataset
- Sample chest X-ray images (Normal vs Pneumonia)  
- You can download publicly available datasets like [Kaggle Chest X-Ray Pneumonia Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)  
- Place your dataset in the `data/` folder and adjust paths in `train_cnn.py` accordingly  

---

## Installation

### Clone Repository
```bash
git clone https://github.com/<USERNAME>/chest-xray-classifier.git
cd chest-xray-classifier
```

## Conclusion

The **chest-xray-classifier** project demonstrates an end-to-end pipeline for classifying chest X-ray images using a custom CNN built from scratch in NumPy. It showcases both machine learning implementation and full-stack integration, providing a working web interface for real-time predictions. This project highlights skills in **CNN design, Python programming, and full-stack deployment**.

