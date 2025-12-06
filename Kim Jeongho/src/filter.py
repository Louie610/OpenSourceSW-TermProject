from typing import Tuple

import cv2
import numpy as np

def apply_cartoon_filter(img: np.ndarray) -> np.ndarray:
    """
    Apply a cartoon-style filter to the input image.

    Steps:
    1. Smooth colors with bilateral filter (noise reduction).
    2. Detect edges using adaptive thresholding.
    3. Combine smoothed colors and edges.
    """
    color = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 7)

    edges = cv2.adaptiveThreshold(
        gray_blur,
        maxValue=255,
        adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
        thresholdType=cv2.THRESH_BINARY,
        blockSize=9,
        C=2,
    )

    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    cartoon = cv2.bitwise_and(color, edges_bgr)
    return cartoon

def apply_sketch_filter(img: np.ndarray) -> np.ndarray:
    """
    Apply a pencil-sketch-style filter to the input image.

    Steps:
    1. Convert to grayscale.
    2. Invert and blur the image.
    3. Blend original grayscale and blurred inverted image (dodge blend).
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, ksize=(21, 21), sigmaX=0)

    sketch = cv2.divide(gray, 255 - blur, scale=256.0)

    return sketch
