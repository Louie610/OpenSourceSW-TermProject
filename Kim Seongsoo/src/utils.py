import cv2
import numpy as np

def load_image(path):
    """Load image from ANY path including Korean paths."""
    try:
        with open(path, "rb") as f:
            data = f.read()

        img_array = np.frombuffer(data, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if img is None:
            raise FileNotFoundError(f"Cannot decode image: {path}")

        return img
    except Exception as e:
        raise FileNotFoundError(f"Cannot load image: {path}\n{e}")


def save_image(path, img):
    """Save image even with Korean paths."""
    ext = path.split('.')[-1]  
    _, encoded_img = cv2.imencode(f".{ext}", img)
    with open(path, "wb") as f:
        encoded_img.tofile(f)
