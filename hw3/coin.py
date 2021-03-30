import color_table as ct
import cv2
import numpy as np


def get_color_and_value(side_len):
    """
    Args:
        side_len: side length of a connected component

    Returns:
        the corresponding color and coin value of the component,
        50-dollar: green and value 50,
        10-dollar: yellow and value 10,
        5-dollar: orange and value 5,
        1-dollar: red and value 1.
    """

    color, value = ct.white, 0
    if side_len >= 117:
        color, value = ct.green, 50
    elif side_len >= 100:
        color, value = ct.yellow, 10
    elif side_len >= 90:
        color, value = ct.orange, 5
    else:
        color, value = ct.red, 1

    return color, value  # end get_color_and_value


def threshold_binary(src_img, threshold):
    _, bin_img = cv2.threshold(src_img, threshold, 255, cv2.THRESH_BINARY)
    return bin_img


def clean_background_and_inner(origin):
    """
    Takes the coin with background and inner black noises,
    clean them and return the clean coin back.
    """

    # Turn the coin into gray first. Binarization once but coins connect together.
    # So blur and use more erode than dilate to shrink coin circle and clean noises.
    # Another binarization with higher threshold value is used to get the coin back.

    gray = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)

    bin = threshold_binary(gray, 70)
    cv2.imwrite('coin_pic/bin.jpg', bin)

    blur = cv2.GaussianBlur(bin, (5, 5), 0)

    adjust = cv2.erode(blur, np.ones((3, 3)), iterations=10)
    adjust = cv2.dilate(adjust, np.ones((3, 3)), iterations=5)

    clean = threshold_binary(adjust, 150)

    return clean  # end background_and_inner_clean


def get_coin() -> None:
    # height = 4000, width = 2250
    coin = cv2.imread('coin_pic/coin.jpg')

    # this variable coin will later be used as the target_img, add in rectangles and text.
    coin = cv2.resize(coin, (1000, 562))

    clean = clean_background_and_inner(coin)
    cv2.imwrite('coin_pic/clean.jpg', clean)

    num_labels, _, stats, _ = cv2.connectedComponentsWithStats(clean, connectivity=8, ltype=cv2.CV_32S)

    total_value = 0

    # stats[0] is the background, stats[15] is a small noise spot at the lower left
    for stat in stats[1:15]:
        # (x, y) is the upper-left coord.
        x, y, width, height, area = map(int, stat)

        color, value = get_color_and_value(max(width, height))
        total_value += value

        cv2.rectangle(coin,  # target_img
                      (x - 10, y - 10),  # upper-left coord.
                      (x + width + 10, y + height + 10),  # lower-right coord.
                      color, 1, cv2.LINE_AA)  # color, [border-thickness, [line-type]]

    cv2.putText(coin,  # target_img
                f'coin value = {total_value}',  # text
                (50, 50),  # start coord.
                cv2.FONT_HERSHEY_SIMPLEX,  # font style
                1, ct.white, 1, cv2.LINE_AA)  # font size, color, [thickness, [line-type]]

    cv2.imwrite('coin_pic/get.jpg', coin)

    return  # end get_coin


if __name__ == '__main__':
    get_coin()
