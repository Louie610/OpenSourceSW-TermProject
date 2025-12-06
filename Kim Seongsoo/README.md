# Pencil Sketch Image Filter (OpenCV)
Author: Kim Seongsoo

This project is an open-source software that converts an input image into a pencil sketch style using Python and OpenCV.  
The effect is produced using Grayscale conversion, Gaussian Blur, and Divide Blending.

---

## Demo

Input image: `images/input_example.jpg`  
Output image: `images/output_sketch.png`

---

## How to Run

### 1. Install required packages

### 2. Run the main script
The script runs with default input and output paths.

### 3. Specify input image

### 4. Specify output path

### 5. Adjust blur intensity

---

## Features

1. Implementation of a pencil sketch filter using:
   - Grayscale conversion  
   - Gaussian Blur  
   - Divide blending technique  

2. Supports Korean file paths and OneDrive directories  
   - The default OpenCV `imread()` function fails on Korean paths  
   - This project uses binary file reading + `cv2.imdecode()` to ensure compatibility

3. Command-line interface options  
   - `--input`: Path to input image  
   - `--output`: Path to save output image  
   - `--blur`: Gaussian blur kernel size  

4. Easily extendable  
   - Additional filters (cartoon, edge-detection, etc.) can be added  
   - Possible to create GUI or real-time webcam sketch mode

---

## Algorithm Overview

1. Load input image  
2. Convert to grayscale  
3. Apply Gaussian blur  
4. Generate sketch using divide blending  
5. Save output image  

---

## References

- OpenCV Documentation  
- Image filtering and blending tutorials  
- Python OpenCV community examples  

