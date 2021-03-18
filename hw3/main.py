import cv2
import numpy as np

def get_coin() -> None:
    coin = cv2.imread('pic/coin.jpg')
    coin_gray = cv2.cvtColor(coin, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('pic/coin_gray.jpg', coin_gray)

    coin_canny = cv2.Canny(coin_gray, 50, 150)
    cv2.imwrite('pic/coin_canny.jpg', coin_canny)

    ret, coin_bin = cv2.threshold(coin_gray, 60, 255, cv2.THRESH_BINARY)
    cv2.imwrite('pic/coin_bin.jpg', coin_bin)

    coin_erode = cv2.erode(coin_bin, np.ones((3, 3)), iterations=5)
    cv2.imwrite('pic/coin_erode.jpg', coin_erode)

    coin_dilate = cv2.dilate(coin_bin, np.ones((2, 2)), iterations=1)
    cv2.imwrite('pic/coin_dilate.jpg', coin_dilate)


    coin_erode_2 = cv2.erode(coin_dilate, np.ones((3, 3)), iterations=5)
    cv2.imwrite('pic/coin_erode_2.jpg', coin_erode_2)

# end coin section

def get_floor() -> None:
    floor = cv2.imread('pic/floor.jpg')




def main() -> None:
    get_coin()
    get_floor()
    return


if __name__ == '__main__':
    main()
