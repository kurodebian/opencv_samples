import numpy as np
import cv2


#def to_grayscale(path):
img = cv2.imread('apple.jpg')
out = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("tes", out)
cv2.waitKey(0)
#    return grayed

#to_grayscale("apple.jpg")
