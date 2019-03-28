import numpy as np
import cv2


def replace(value, bit):
    assert bit in [0, 1]
    return (value >> 1 << 1) + bit


def binarize(image):
    if len(image.shape) != 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)
    return thresh // 255


def hide(image, target):
    assert image.shape == target.shape
    h, w = image.shape[:2]
    target = binarize(target)

    out = np.zeros_like(image, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            out[i, j] = replace(image[i, j], target[i, j])
    return out
