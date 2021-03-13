import cv2
import numpy as np

def get_rid_of_black_spot(show: bool = False) -> np.ndarray:
    circle_gray = cv2.imread('pic/circle.png', cv2.COLOR_BGR2GRAY)

    ret, circle_bin = cv2.threshold(circle_gray, 127, 255, cv2.THRESH_BINARY)
    circle_dilate = cv2.dilate(circle_bin, np.ones((5, 6)), iterations=5)
    circle_erode = cv2.erode(circle_dilate, np.ones((5, 6)), iterations=5)

    if show:
        cv2.imwrite('pic/circle_gray.png', circle_gray)
        cv2.imwrite('pic/circle_bin.png', circle_bin)
        cv2.imwrite('pic/circle_dilate.png', circle_dilate)

    return circle_erode


def get_border_line(show: bool = False) -> np.ndarray:
    man_gray = cv2.imread('pic/man.png', cv2.COLOR_BGR2GRAY)

    ret, man_bin = cv2.threshold(man_gray, 127, 255, cv2.THRESH_BINARY)
    man_erode = cv2.erode(man_bin, np.ones((3, 3)), iterations=4)

    if show:
        cv2.imwrite('pic/man_gray.png', man_gray)
        cv2.imwrite('pic/man_bin.png', man_bin)
        cv2.imwrite('pic/man_erode.png', man_erode)

    return man_bin - man_erode


def main() -> None:
    circle_erode = get_rid_of_black_spot(show=True)
    cv2.imwrite('pic/circle_erode.png', circle_erode)

    man_border = get_border_line(show=True)
    cv2.imwrite('pic/man_border.png', man_border)


if __name__ == '__main__':
    main()
