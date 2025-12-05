import cv2
import numpy as np

def to_gray(img):
    """흑백 필터"""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def blur(img, k=7):
    """블러 필터"""
    return cv2.GaussianBlur(img, (k, k), 0)

def edge(img):
    """엣지(윤곽선) 필터"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(gray, 100, 200)

def cartoon(img):
    """간단 카툰 필터"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9, 10
    )
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon_img = cv2.bitwise_and(color, color, mask=edges)
    return cartoon_img