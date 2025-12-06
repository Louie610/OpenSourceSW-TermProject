# Cartoon & Sketch Image Filter (OpenCV)

## Overview
This project provides two image filters implemented with OpenCV:

• Cartoon filter: smooth color + edge enhancement  
• Sketch filter: pencil drawing effect using grayscale and dodge blend  

Users can run the program with command-line arguments and choose a filter mode.

## Demo
Input image: images/input_example.jpg  
Cartoon output: images/output_cartoon.png  
Sketch output: images/output_sketch.png  

## Project Structure
Kim Jeongho/
  images/
    input_example.jpg
    output_cartoon.png
    output_sketch.png
  src/
    main.py
    filter.py
    utils.py
  requirements.txt
  README.md

## Requirements
Python 3.10+  
opencv-python  
numpy  

## Installation
pip3 install -r requirements.txt

## How to Run

Cartoon filter:
python3 src/main.py --input images/input_example.jpg --output images/output_cartoon.png --mode cartoon

Sketch filter:
python3 src/main.py --input images/input_example.jpg --output images/output_sketch.png --mode sketch

## Notes
• Output file directory is created automatically if needed  
• Only 'cartoon' and 'sketch' modes are supported  
• Input image path must be valid
