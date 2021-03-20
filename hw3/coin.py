import cv2
import numpy as np

def get_coin() -> None:
    # height = 4000, width = 2250
    coin = cv2.imread('pic/coin.jpg')

    coin = cv2.resize(coin, (1000, 562))
    cv2.imwrite('pic/coin_resize.jpg', coin)
    coin_copy = coin.copy()

    coin_gray = cv2.cvtColor(coin, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('pic/coin_gray.jpg', coin_gray)

    _, coin_bin = cv2.threshold(coin_gray, 70, 255, cv2.THRESH_BINARY)
    cv2.imwrite('pic/coin_bin.jpg', coin_bin)

    coin_blur = cv2.GaussianBlur(coin_bin, (5, 5), 0)

    coin_erode = cv2.erode(coin_blur, np.ones((3, 3)), iterations=10)
    coin_erode = cv2.dilate(coin_erode, np.ones((3, 3)), iterations=5)

    _, coin_blur = cv2.threshold(coin_erode, 150, 255, cv2.THRESH_BINARY)
    cv2.imwrite('pic/blur.jpg', coin_blur)

    coin_erode = cv2.dilate(coin_blur, np.ones((2, 2)), iterations=3)
    cv2.imwrite('pic/coin_erode.jpg', coin_erode)

    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(coin_erode, connectivity=8, ltype=cv2.CV_32S)

    red = (0, 0, 255) # 1 dollar
    orange = (0, 97, 255) # 5 dollar
    yellow = (0, 255, 255) # 10 dollar
    green = (0, 255, 0) # 50 dollar
    coin_value = 0

    for i in range(1, num_labels):
        # (a, b) is the upper-left coord.
        a, b, width, height, area = map(int, stats[i])
        x, y = map(int, centroids[i])
        color = (0, 0, 0)
        if area < 4000:
            continue
        if width >= 120 or height >= 120:
            color = green
            coin_value += 50
        elif width >= 100 or height >= 100:
            color = yellow
            coin_value += 10
        elif width >= 90 or height >= 90:
            color = orange
            coin_value += 5
        else:
            color = red
            coin_value += 1

        # (target_img, upper-left coord., lower-right coord., color, [border-thickness, [line-type]])
        cv2.rectangle(coin_copy, (a-10, b-10), (a+width+10, b+height+10), color, 1, cv2.LINE_AA)

        # (target_img, message, start coord., font-style, font-size, color, [thickness, [line-type]])

    cv2.putText(coin_copy,  f'coin value = {coin_value}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 150, 200), 1, cv2.LINE_AA)
    cv2.imwrite('pic/coin_copy.jpg', coin_copy)

# end coin section

if __name__ == '__main__':
    get_coin()
