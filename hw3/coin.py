import cv2
import color_table as ct
import numpy as np

def get_coin() -> None:
    # height = 4000, width = 2250
    coin = cv2.imread('pic/coin.jpg')

    coin = cv2.resize(coin, (1000, 562))
    cv2.imwrite('pic/coin_resize.jpg', coin)

    coin_adjust = coin_background_and_inner_clean(coin)

    num_labels, _, stats, _ = cv2.connectedComponentsWithStats(coin_adjust, connectivity=8, ltype=cv2.CV_32S)

    coin_value = 0
    result_target_coin = cv2.imread('pic/coin_resize.jpg')

    # stats[0] is the background
    for stat in stats[1:]:
        # (x, y) is the upper-left coord.
        x, y, width, height, area = map(int, stat)
        color = (0, 0, 0)
        side_len = max(width, height)
        if area < 4000:
            continue
        if side_len >= 120:
            color = ct.green
            coin_value += 50
        elif side_len >= 100:
            color = ct.yellow
            coin_value += 10
        elif side_len >= 90:
            color = ct.orange
            coin_value += 5
        else:
            color = ct.red
            coin_value += 1

        # (target_img, upper-left coord., lower-right coord., color, [border-thickness, [line-type]])
        cv2.rectangle(result_target_coin, (x - 10, y - 10), (x + width + 10, y + height + 10), color, 1, cv2.LINE_AA)

    # (target_img, message, start coord., font-style, font-size, color, [thickness, [line-type]])
    cv2.putText(result_target_coin, f'coin value = {coin_value}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, ct.white, 1, cv2.LINE_AA)
    cv2.imwrite('pic/coin_get.jpg', result_target_coin)

    return  # end get_coin

def coin_background_and_inner_clean(coin_origin):
    coin_gray = cv2.cvtColor(coin_origin, cv2.COLOR_BGR2GRAY)

    _, coin_bin = cv2.threshold(coin_gray, 70, 255, cv2.THRESH_BINARY)
    cv2.imwrite('pic/coin_bin.jpg', coin_bin)

    coin_blur = cv2.GaussianBlur(coin_bin, (5, 5), 0)

    coin_adjust = cv2.erode(coin_blur, np.ones((3, 3)), iterations=10)
    coin_adjust = cv2.dilate(coin_adjust, np.ones((3, 3)), iterations=5)

    _, coin_adjust = cv2.threshold(coin_adjust, 150, 255, cv2.THRESH_BINARY)

    coin_adjust = cv2.dilate(coin_adjust, np.ones((2, 2)), iterations=3)
    cv2.imwrite('pic/coin_adjust.jpg', coin_adjust)

    return coin_adjust  # end coin_background_and_inner_clean

if __name__ == '__main__':
    get_coin()
