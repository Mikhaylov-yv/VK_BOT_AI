import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('https://cdn4.img.ria.ru/images/151946/71/1519467104.jpg',0)          # queryImage
img2 = cv2.imread('https://i.msmap.ru/1/2/9/4/5/thumbs/600_375_fixw.jpg',0) # trainImage

# Initiate SIFT detector
orb = cv2.ORB()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

