# Cartoon & Sketch Image Filter (OpenCV)

## Overview
This project provides two image filters implemented using OpenCV:

• Cartoon filter: smooth color + edge enhancement  
• Sketch filter: pencil-style drawing effect using grayscale and dodge blending  

The program supports a command-line interface where users can specify the input path,
output path, and filter mode. Input validation, automatic directory creation, and detailed
error handling are included to ensure reliable execution


## Demo
Input image:
    images/input_example.jpg

Output examples:
    images/output_cartoon.png  
    images/output_sketch.png  


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
Install required packages:

pip3 install -r requirements.txt


## How to Run

Cartoon filter:
python3 src/main.py --input images/input_example.jpg --output images/output_cartoon.png --mode cartoon

Sketch filter:
python3 src/main.py --input images/input_example.jpg --output images/output_sketch.png --mode sketch


## Filter Implementation Details

### Cartoon Filter (filter.py)
Steps:
1. Smooth colors using bilateral filtering  
2. Convert to grayscale and reduce noise with median blur  
3. Detect edges using adaptive thresholding  
4. Combine smoothed colors with edge map  


### Sketch Filter (filter.py)
Steps:
1. Convert to grayscale  
2. Invert the grayscale image  
3. Blur the inverted image  
4. Perform dodge blend: gray / (255 - blur)  


## Program Flow (main.py)
1. Parse command-line arguments (`--input`, `--output`, `--mode`)  
2. Validate paths and create output directory if necessary  
3. Read input image and raise error if loading fails  
4. Choose filter based on mode (`cartoon` or `sketch`)  
5. Save output image and check for save errors  


## Notes
• Output file directory is created automatically if needed
• Only "cartoon" and "sketch" modes are supported 
• Input image path must be valid
• Detailed error handling is implemented