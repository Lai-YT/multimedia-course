import cv2
import numpy as np

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
