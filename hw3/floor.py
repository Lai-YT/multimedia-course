import color_table as ct
import cv2
import numpy as np

def threshold_binary(src_img, threshold):
    _, bin_img = cv2.threshold(src_img, threshold, 255, cv2.THRESH_BINARY)
    return bin_img

def get_floor() -> None:
    floor = cv2.imread('floor_pic/floor.jpg')

    # the variable floor will later be used as the target_img, drawing line on.
    floor = cv2.resize(floor, (562, 1000))

    gray = cv2.cvtColor(floor, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('floor_pic/gray.jpg', gray)

    bin = threshold_binary(gray, 100)

    blur = cv2.GaussianBlur(bin, (3, 3), 0)
    cv2.imwrite('floor_pic/blur.jpg', blur)

    # upper left area [:200, 200:] is a bit special, so use another threshold
    bin = threshold_binary(blur, 160)
    bin[:200, 200:] = threshold_binary(blur[:200, 200:], 240)
    cv2.imwrite('floor_pic/bin.jpg', bin)

    # get contour line
    canny = cv2.Canny(bin, 50, 150)
    cv2.imwrite('floor_pic/canny.jpg', canny)

    lines = cv2.HoughLines(canny, 1, np.pi/4, 250)
    for line in lines:
        rho, theta = line[0]
        a, b = np.cos(theta), np.sin(theta)
        x0, y0 = a * rho, b * rho
        x1, y1 = int(x0 + 1000 * (-b)), int(y0 + 1000 * (a))
        x2, y2 = int(x0 - 1000 * (-b)), int(y0 - 1000 * (a))

        cv2.line(floor, #  target_img
                 (x1, y1), #  left-start coord.
                 (x2, y2), #  right-end coord.
                 ct.red, 1, cv2.LINE_AA) #  color, [border-thickness, [line-type]]

    cv2.imwrite('floor_pic/line.jpg', floor)

    return #  end get_floor


if __name__ == '__main__':
    get_floor()
