import cv2
import numpy as np

origin_img = cv2.imread('pic/donut.jpg')
height = origin_img.shape[0] # 823
width = origin_img.shape[1] # 936

# ----------

gray_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('pic/gary.jpg', gray_img)

ycrcb_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2YCrCb)
cv2.imwrite('pic/ycrcb.jpg', ycrcb_img)

hsv_img = cv2.cvtColor(origin_img, cv2.COLOR_BGR2HSV)
cv2.imwrite('pic/hsv.jpg', hsv_img)

# -----techs-----
# An image is a 3-dimensinal numpy array of the form [pixels in height, pixels in width, number of channels],
# a color image has 3 channels, 0-blue, 1-green, 2-red; a gray image has only one channel.

# -----bgr-gray-----
# [:, :, n] means to keep the height and width, but channel n only. So is a gray image.

blue_gray_img = cv2.imwrite('pic/blue_gray.jpg', origin_img[:, :, 0])
green_gray_img = cv2.imwrite('pic/green_gray.jpg', origin_img[:, :, 1])
gred_gray_img = cv2.imwrite('pic/red_gray.jpg', origin_img[:, :, 2])

# -----bgr-color-----
# If wan the blue-color-only image, let [:, :, 1] and [:, :, 2] be all zeros.
# Since still has 3 channels, it's a color image.

# create a template image with three channels all zero: black image
template_img = np.zeros((height, width, 3), np.uint8)
cv2.imwrite('pic/template.jpg', template_img)

blue_color_img = template_img.copy()
# get color blue
blue_color_img[:, :, 0] = origin_img[:, :, 0]
cv2.imwrite('pic/blue_color.jpg', blue_color_img)

green_color_img = template_img.copy()
# get color green
green_color_img[:, :, 1] = origin_img[:, :, 1]
cv2.imwrite('pic/green_color.jpg', green_color_img)

red_color_img = template_img.copy()
# get color red
red_color_img[:, :, 2] = origin_img[:, :, 2]
cv2.imwrite('pic/red_color.jpg', red_color_img)

# -----shape-drawing-----

draw_img = origin_img

# (target_img, left-start cord., right-end cord., color, border-thickness)
cv2.line(draw_img, (height//2, 10), (10, width//2), (50, 150, 200), 5)

# (target_img, upper-left cord., lower-right cord., color, border-thickness)
cv2.rectangle(draw_img, (80, 550), (350, 800), (0, 200, 200), 5)

# (target_img, center cord., radius, color, border-thickness)
cv2.circle(draw_img, (width//2 + 290, height//2 + 10), 350, (150, 0, 250), 5)
cv2.circle(draw_img, (width//2 + 290, height//2 + 10), 100, (200, 0, 200), -1)

# note that border-thickness = -1 means to fill up the shape

# -----text-----

text = 'donuts!'
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
# (target_img, message, start cord., font-style, font-size, color, thickness)
cv2.putText(draw_img, text, (120, 200), font, 10, (255, 100, 200), 5)
cv2.imwrite('pic/draw.jpg', draw_img)
