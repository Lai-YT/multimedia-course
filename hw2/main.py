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
