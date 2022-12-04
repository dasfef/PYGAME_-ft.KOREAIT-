import numpy as np
import itertools
import matplotlib.pyplot as plt

TILE_WIDTH = 128
TILE_HEIGHT = 256

image = np.zeros((TILE_HEIGHT, TILE_WIDTH, 4), np.uint8)
height, width = image.shape[:2]
color_top = [255, 0, 0, 255]
color_left = [0, 255, 0, 255]
color_right = [0, 0, 255, 255]


# =================== tile Color ====================
tx = width / 2
ty = np.sin(np.pi / 6) * tx
ty2 = height - ty

for x, y in itertools.product(range(width), range(height)) :
    if np.abs(x - tx) / tx + np.abs(y - ty) / ty <= 1 :
        image[y, x, :] = color_top
    elif ty <= y <= height - ty and x < tx :
        image[y, x, :] = color_left
    elif ty <= y <= height - ty and x >= tx :
        image[y, x, :] = color_right
    elif np.abs(x - tx) / tx + np.abs(y - ty2) / ty <= 1 and x < tx :
        image[y, x, :] = color_left
    elif np.abs(x - tx) / tx + np.abs(y - ty2) / ty <= 1 and x >= tx :
        image[y, x, :] = color_right

plt.imsave("test.png", image)