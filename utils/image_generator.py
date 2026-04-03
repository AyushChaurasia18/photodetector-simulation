import numpy as np
import cv2

def generate_default_image(size=256):
    img = np.zeros((size, size), dtype=np.float32)

    # sky background (gradient)
    for i in range(size):
        img[i, :] = 0.3 + 0.3 * (i / size)

    # ground
    img[int(size*0.7):, :] = 0.2

    # house base (rectangle)
    cv2.rectangle(img, (80, 140), (180, 220), 0.8, -1)

    # roof (triangle)
    pts = np.array([[80,140],[130,90],[180,140]], np.int32)
    cv2.fillPoly(img, [pts], 0.6)

    # door
    cv2.rectangle(img, (115, 170), (145, 220), 0.3, -1)

    # window
    cv2.rectangle(img, (95, 160), (115, 180), 0.1, -1)

    # sun (circle)
    cv2.circle(img, (200, 50), 20, 1.0, -1)

    return img