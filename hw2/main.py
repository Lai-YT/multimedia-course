import cv2
import numpy as np

circle = cv2.imread('pic/circle.png', cv2.COLOR_BGR2GRAY)
cv2.imshow('circle', circle)

ret, circle_bin = cv2.threshold(circle, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('circle_bin', circle_bin)

circle_dilate = cv2.dilate(circle, np.ones((6, 6)), iterations=5)
cv2.imshow('circle_dilate', circle_dilate)

circle_erode = cv2.erode(circle_dilate, np.ones((6, 6)), iterations=5)
cv2.imshow('circle_erode', circle_erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
