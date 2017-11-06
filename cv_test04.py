#!/usr/bin/python
# -*- coding: <encoding name> -*-

import cv2
import numpy as np

img = cv2.imread('apple.jpg')
detector = cv2.FastFeatureDetector_create() #'ORB')
keypoints = detector.detect(img)
out = cv2.drawKeypoints(img, keypoints, None)
cv2.imshow("SHOW KEYPOINTS IMAGE", out)
cv2.waitKey(0)
