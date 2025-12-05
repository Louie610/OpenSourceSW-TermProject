# Cartoon & Sketch Image Filter with OpenCV

## Overview
This project implements simple cartoon and sketch image filters using OpenCV.  
The user can choose one of the two modes and generate a filtered image from a given input image.

## Features
- `cartoon` mode: cartoon-style image using bilateral filter and edge detection
- `sketch` mode: pencil-sketch-style image using grayscale, inversion and dodge blend

## Demo
- Input: `images/input_example.jpg`
- Cartoon output: `images/output_cartoon.png`
- Sketch output: `images/output_sketch.png`

## Requirements
- Python 3.10+
- opencv-python
- numpy

## How to Install
```bash
pip3 install -r requirements.txt
