# Image Filter Project

This repository contains three independent image filter implementations developed by Team 44. Each member implemented different filters using OpenCV in Python. All work is organized in separate directories so that each member's project can run independently.


## Project Overview

The project includes multiple image processing filters such as:
- Cartoon filter
- Sketch filter
- Blur / Edge / Grayscale filters

Each member implemented different filters using OpenCV in Python.


## Team Members

1. Kim Jeongho – Folder: Kim Jeongho/
   - Louie implemented the cartoon and sketch filters using OpenCV and designed the main program structure, including command-line execution and mode selection logic. He also prepared the example input/output images and organized the overall folder structure for the team project.

2. Kim Seongsoo – Folder: Kim Seongsoo/
   - This program automatically generates a pencil sketch effect from an input image using Gaussian blur and color decomposition techniques. When running main.py, default input and output paths are automatically configured, and the user can adjust the image path and blur intensity through command-line options. The overall structure consists of utils.py for image I/O processing and filter.py for implementing the sketch algorithm, with all files organized within the Kim Seongsoo folder.

3. Lee Hyewon – Folder: Lee Hyewon/
   - Lee Hyewon folder contains the Image Filter program, including the main Python script, filter functions, and sample output images. It also includes a README documenting the project setup, usage instructions, and results. All required files for running and reviewing the project are located here.

Each member folder contains:
- Source code
- Example input/output images
- Member-specific README.md
- requirements.txt listing required packages


## Demo Examples

Each member provides example input and output images in their own `images/` directory.
Typical examples include:

- Kim Jeongho: input_example.jpg, output_cartoon.png, output_sketch.png
- Kim Seongsoo: input_example.jpg, output_sketch.png
- Lee Hyewon: sample.jpeg, output_blur.png, output_cartoon.png, output_edge.png, output_gray.png

For more details, please refer to each member’s README.md.


## Dependencies

Required Python packages are listed individually inside each member's requirements.txt file.


## How to Run

Each member provides an independent implementation.  
Navigate into a member folder and run their main script.

General form:
    python3 main.py --input <input_path> --output <output_path> --mode <filter>

Exact commands vary by member.  
Refer to each folder’s README.md.


## Additional Information

The file "Team44_info.txt" contains the repository link, team member list, and required submission information.