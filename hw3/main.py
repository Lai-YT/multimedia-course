import cv2
import numpy as np

def get_coin() -> None:
    # height = 4000, width = 2250
    coin = cv2.imread('pic/coin.jpg')

    coin = cv2.resize(coin, (1000, 562))
    cv2.imwrite('pic/coin_resize.jpg', coin)

    coin_gray = cv2.cvtColor(coin, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('pic/coin_gray.jpg', coin_gray)

    _, coin_bin = cv2.threshold(coin_gray, 70, 255, cv2.THRESH_BINARY)
    cv2.imwrite('pic/coin_bin.jpg', coin_bin)

    # coin_bin = cv2.erode(coin_bin, np.ones((2, 2)), iterations=3)

    coin_blur = cv2.medianBlur(coin_bin, 1)
    coin_blur = cv2.GaussianBlur(coin_blur, (5, 5), 0)
    print(coin_blur)
    # _, coin_blur = cv2.threshold(coin_blur, 127, 255, cv2.THRESH_BINARY)
    # cv2.imwrite('pic/blur.jpg', coin_blur)

    coin_erode = cv2.erode(coin_blur, np.ones((3, 3)), iterations=10)
    coin_erode = cv2.dilate(coin_erode, np.ones((3, 3)), iterations=5)

    _, coin_blur = cv2.threshold(coin_erode, 150, 255, cv2.THRESH_BINARY)
    cv2.imwrite('pic/blur.jpg', coin_blur)

    coin_erode = cv2.dilate(coin_blur, np.ones((2, 2)), iterations=3)


    cv2.imwrite('pic/coin_erode.jpg', coin_erode)


    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(coin_erode, connectivity=8, ltype=cv2.CV_32S)
    print(num_labels)

# end coin section

def get_floor() -> None:
    floor = cv2.imread('pic/floor.jpg')




def main() -> None:
    get_coin()
    get_floor()
    return


if __name__ == '__main__':
    main()
