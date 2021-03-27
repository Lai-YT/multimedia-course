import color_table as ct
import cv2
import numpy as np

def get_coin_2() -> None:
    coin = cv2.imread('coin2_pic/coin2.jpg')

    coin = cv2.resize(coin, (1000, 562))
    cv2.imwrite('coin2_pic/coin2_resize.jpg', coin)

    coin_adjust = coin_inner_clean(coin)
    cv2.imwrite('coin2_pic/coin2_adjust.jpg', coin_adjust)

    num_labels, _, stats, _ = cv2.connectedComponentsWithStats(coin_adjust, connectivity=8, ltype=cv2.CV_32S)

    coin_value = 0
    result_target_coin = cv2.imread('coin2_pic/coin2_resize.jpg')

    for stat in stats[1:]:
        x, y, width, height, area = map(int, stat)
        color = (0, 0, 0)
        side_len = max(width, height)

        if side_len >= 440:
            color = ct.white
            coin_value += 1000
        elif side_len >= 420:
            color = ct.purple
            coin_value += 500
        elif side_len >= 410:
            color = ct.blue
            coin_value += 100
        elif side_len >= 70:
            color = ct.green
            coin_value += 50
        elif side_len >= 60:
            color = ct.yellow
            coin_value += 10
        elif side_len >= 50:
            color = ct.orange
            coin_value += 5
        else:
            color = ct.red
            coin_value += 1

        # (target_img, upper-left coord., lower-right coord., color, [border-thickness, [line-type]])
        cv2.rectangle(result_target_coin, (x - 10, y - 10), (x + width + 10, y + height + 10), color, 1, cv2.LINE_AA)

    # (target_img, message, start coord., font-style, font-size, color, [thickness, [line-type]])
    cv2.putText(result_target_coin, f'coin value = {coin_value}', (50, 512), cv2.FONT_HERSHEY_SIMPLEX, 1, ct.white, 1, cv2.LINE_AA)
    cv2.imwrite('coin2_pic/coin2_get.jpg', result_target_coin)

    return #  end get_coin_2,

def coin_inner_clean(coin_origin):
    coin_gray = cv2.cvtColor(coin_origin, cv2.COLOR_BGR2GRAY)

    _, coin_bin = cv2.threshold(coin_gray, 70, 255, cv2.THRESH_BINARY)
    cv2.imwrite('coin2_pic/coin2_bin.jpg', coin_bin)

    coin_blur = cv2.GaussianBlur(coin_bin, (9, 9), 5)
    # cv2.imwrite('coin2_pic/coin2_blur.jpg', coin_blur)

    coin_erode = cv2.erode(coin_blur, np.ones((5, 5)), iterations=7)
    # cv2.imwrite('coin2_pic/coin2_erode.jpg', coin_erode)

    coin_dilate = cv2.dilate(coin_erode, np.ones((5, 5)), iterations=5)
    # cv2.imwrite('coin2_pic/coin2_dilate.jpg', coin_dilate)

    _, coin_bin2 = cv2.threshold(coin_dilate, 70, 255, cv2.THRESH_BINARY)

    return coin_bin2 #  end coin_inner_clean

if __name__ == '__main__':
    get_coin()
