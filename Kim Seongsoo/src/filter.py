import cv2

def pencil_sketch(image, blur_ksize=21):
    """
    Pencil sketch filter using grayscale + Gaussian blur + divide blend.
    :param image: input BGR image
    :param blur_ksize: odd number for Gaussian blur size
    :return: sketch-style image (grayscale)
    """
    # 1. Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Gaussian blur (ksize must be odd)
    if blur_ksize % 2 == 0:
        blur_ksize += 1  # ensure odd number
    blurred = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0)

    # 3. Divide blend → sketch effect
    sketch = cv2.divide(gray, blurred, scale=256)

    return sketch