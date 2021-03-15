import cv2
import numpy as np

# -----circle-----

circle_gray = cv2.imread('pic/circle.png', cv2.COLOR_BGR2GRAY)
cv2.imwrite('pic/circle_gray.png', circle_gray)

# image only in black and white
ret, circle_bin = cv2.threshold(circle_gray, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('pic/circle_bin.png', circle_bin)

# using close operation to get rid of small black spot.
# same as dilate first, and than erode, which are the two following lines:

# circle_dilate = cv2.dilate(circle_bin, np.ones((5, 6)), iterations=5)
# circle_unspot = cv2.erode(circle_dilate, np.ones((5, 6)), iterations=5)

circle_unspot = cv2.morphologyEx(circle_bin, cv2.MORPH_CLOSE, np.ones((5, 6)), iterations=5)
cv2.imwrite('pic/circle_unspot.png', circle_unspot)

# -----man-----

man_gray = cv2.imread('pic/man.png', cv2.COLOR_BGR2GRAY)
cv2.imwrite('pic/man_gray.png', man_gray)

# image only in black and white
ret, man_bin = cv2.threshold(man_gray, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('pic/man_bin.png', man_bin)

# using gradient to get the contour line.
# same as dilate - erode, which are the three following lines:

# man_dilate = cv2.dilate(man_bin, np.ones((3, 3)), iterations=2)
# man_erode = cv2.erode(man_bin, np.ones((3, 3)), iterations=2)
# man_border = man_dilate - man_erode

man_border = cv2.morphologyEx(man_bin, cv2.MORPH_GRADIENT, np.ones((3, 3)), iterations=2)
cv2.imwrite('pic/man_border.png', man_border)

# -----image-subtraction----

# 1 is white, 0 and -1 are black
# black - white = 0 - 1 = -1 -> black
# white - black = 1 - 0 = 1 -> white
# black - black = 0 - 0 = 0 -> black
# white - white = 1 - 1 = 0 -> black

# the followings show how subtraction works

black_img = np.zeros((500, 500, 3), np.uint8)
white_img = np.zeros((500, 500, 3), np.uint8)
white_img.fill(255)
bmw = black_img - white_img
wmb = white_img - black_img
bmb = black_img - black_img
wmw = white_img - white_img
cv2.imwrite('pic/black.png', black_img)
cv2.imwrite('pic/white.png', white_img)
cv2.imwrite('pic/bmw.png', bmw)
cv2.imwrite('pic/wmb.png', wmb)
cv2.imwrite('pic/bmb.png', bmb)
cv2.imwrite('pic/wmw.png', wmw)
