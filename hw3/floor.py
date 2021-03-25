import cv2
import numpy as np

def get_floor() -> None:
    floor = cv2.imread('pic/floor.jpg')

    floor = cv2.resize(floor, (562, 1000))
    cv2.imwrite('pic/floor_resize.jpg', floor)

    floor_gray = cv2.cvtColor(floor, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('pic/floor_gray.jpg', floor_gray)

    # print(floor_gray)
    _, floor_bin = cv2.threshold(floor_gray, 100, 255, cv2.THRESH_BINARY)
    cv2.imwrite('pic/floor_bin.jpg', floor_bin)


    # floor_line = cv2.HoughLinesP(floor_gray, )

    return #  end get_floor

if __name__ == '__main__':
    get_floor()
