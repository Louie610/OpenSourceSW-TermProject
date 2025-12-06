## 1. project overview
This project uses Python and OpenCV library to apply various image filters such as grayscale, blur, edge detection, and cartoon effects. When a sample image is provided, the program automaticaly applies selected filters and generates the output result.

## 2. demo images
| Filter Type | Image Link |
|------------|------------|
| Original | [sample.jpeg](https://raw.githubusercontent.com/Louie610/OpenSourceSW-TermProject/main/Lee%20Hyewon/images/sample.jpeg) |
| Grayscale | [output_gray.png](https://raw.githubusercontent.com/Louie610/OpenSourceSW-TermProject/main/Lee%20Hyewon/images/output_gray.png) |
| Blur | [output_blur.png](https://raw.githubusercontent.com/Louie610/OpenSourceSW-TermProject/main/Lee%20Hyewon/images/output_blur.png) |
| Edge Detection | [output_edge.png](https://raw.githubusercontent.com/Louie610/OpenSourceSW-TermProject/main/Lee%20Hyewon/images/output_edge.png) |
| Cartoon Effect | [output_cartoon.png](https://raw.githubusercontent.com/Louie610/OpenSourceSW-TermProject/main/Lee%20Hyewon/images/output_cartoon.png) |

## 3. Dependencies & Version Info
  • Python 3.12
  • OpenCV 4.9.0
  • NumPy 2.0
  
## 4. Run Instructions
open the terminal and navigate to the project directory. Then excute the program: python main.py 
You will see the following message:

```
=== Simple Image Filter ===
1: Grayscale
2: Blur
3: Edge Detection
4: Cartoon
```

Select a filter number:

Once you enter a number, the program will generate the filtered image and save it inside the images/folder as:

```
output_[filter].png
```
## 5. References
	•	OpenCV Official Docs: https://opencv.org/
	•	NumPy Official Docs: https://numpy.org/
	•	GitHub Codespaces Guide: https://docs.github.com/en/codespaces
