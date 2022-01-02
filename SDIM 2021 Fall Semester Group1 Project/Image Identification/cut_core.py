import cv2
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

path = "photo/"
path2 = "Photo-point/"
f = os.listdir(path)
width = 95
height = 95
now = -1
for filename in f:
    now = now + 1
    img = cv2.imread(path + filename)
    plt.imshow(img)
    plt.show()

    for i in range(3):
        for j in range(4):
            imgnow = img[(i + 1) * height: (i + 2) * height, 50 + (j + 1) * width: 50 + (j + 2) * width]
            plt.imshow(imgnow)
            cv2.imwrite(path2 + str(now) + "-" + str(i * 4 + j) + ".jpg", imgnow)
            plt.show()
