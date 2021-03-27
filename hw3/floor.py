import color_table as ct
import cv2
import numpy as np

def get_floor() -> None:
    floor = cv2.imread('floor_pic/floor.jpg')

    floor = cv2.resize(floor, (562, 1000))
    cv2.imwrite('floor_pic/resize.jpg', floor)

    gray = cv2.cvtColor(floor, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('floor_pic/gray.jpg', gray)

    _, bin = cv2.threshold(gray, 95, 255, cv2.THRESH_BINARY)
    cv2.imwrite('floor_pic/bin.jpg', bin)

    blur = cv2.GaussianBlur(bin, (3, 3), 0)
    cv2.imwrite('floor_pic/blur.jpg', blur)

    _, bin = cv2.threshold(blur, 190, 255, cv2.THRESH_BINARY)
    cv2.imwrite('floor_pic/bin.jpg', bin)

    canny = cv2.Canny(bin, 50, 150)
    cv2.imwrite('floor_pic/canny.jpg', canny)

    lines = cv2.HoughLines(canny, 1, np.pi/4, 250)

    with_line = cv2.imread('floor_pic/resize.jpg')

    for line in lines:
        rho, theta = line[0]
        a, b = np.cos(theta), np.sin(theta)
        x0, y0 = a * rho, b * rho
        x1, y1 = int(x0 + 1000 * (-b)), int(y0 + 1000 * (a))
        x2, y2 = int(x0 - 1000 * (-b)), int(y0 - 1000 * (a))
        # (target_img, left-start coord., right-end coord., color, [border-thickness, [line-type]])
        cv2.line(with_line, (x1, y1), (x2, y2), ct.red, 1, cv2.LINE_AA)

    # _, bin = cv2.threshold(blur, 130, 255, cv2.THRESH_BINARY)
    # cv2.imwrite('floor_pic/bin.jpg', bin)
    #
    # canny = cv2.Canny(bin, 50, 150)
    # cv2.imwrite('floor_pic/canny.jpg', canny)
    #
    # lines = cv2.HoughLines(canny, 1, np.pi/4, 250)
    #
    # for line in lines:
    #     rho, theta = line[0]
    #     a, b = np.cos(theta), np.sin(theta)
    #     x0, y0 = a * rho, b * rho
    #     x1, y1 = int(x0 + 1000 * (-b)), int(y0 + 1000 * (a))
    #     x2, y2 = int(x0 - 1000 * (-b)), int(y0 - 1000 * (a))
    #     # (target_img, left-start coord., right-end coord., color, [border-thickness, [line-type]])
    #     cv2.line(with_line, (x1, y1), (x2, y2), ct.red, 1, cv2.LINE_AA)

    cv2.imwrite('floor_pic/line.jpg', with_line)

    return #  end get_floor

if __name__ == '__main__':
    get_floor()
