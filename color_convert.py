import cv2
import numpy as np

origin_img = cv2.imread('pic/donut.jpg')

# ----------

gray_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('pic/gary.jpg', gray_img)

ycrcb_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2YCrCb)
cv2.imwrite('pic/ycrcb.jpg', ycrcb_img)

hsv_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2HSV)
cv2.imwrite('pic/hsv.jpg', hsv_img)

# -----bgr-gray-----

blue_gray_img = cv2.imwrite('pic/blue_gray.jpg', origin_img[:, :, 0])
ggreen_gray_img = cv2.imwrite('pic/green_gray.jpg', origin_img[:, :, 1])
gred_gray_img = cv2.imwrite('pic/red_gray.jpg', origin_img[:, :, 2])

# -----bgr-color-----

height = origin_img.shape[0]
weight = origin_img.shape[1]
template_img = np.zeros((height, weight, 3), np.uint8)

blue_color_img = template_img.copy()
blue_color_img[:, :, 0] = origin_img[:, :, 0]
cv2.imwrite('pic/blue_color.jpg', blue_color_img)

green_color_img = template_img.copy()
green_color_img[:, :, 1] = origin_img[:, :, 1]
cv2.imwrite('pic/green_color.jpg', green_color_img)

red_color_img = template_img.copy()
red_color_img[:, :, 2] = origin_img[:, :, 2]
cv2.imwrite('pic/red_color.jpg', red_color_img)
