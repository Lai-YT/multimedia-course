import cv2
import numpy as np

def get_apple() -> None:
    apple = cv2.imread('pic/apple.jpg')
    orange = cv2.imread('pic/orange.jpg')

    for i in range(3):
        apple = cv2.pyrDown(apple)
        apple = cv2.resize(apple, (512, 512))
        orange = cv2.pyrDown(orange)
        orange = cv2.resize(orange, (512, 512))
    apple_down = apple
    orange_down = orange
    cv2.imwrite('pic/apple_down.jpg', apple_down)
    cv2.imwrite('pic/orange_down.jpg', orange_down)

    x = 0
    y = 0
    w = 256
    h = 512
    
    apple_cut = apple_down[y:y+h, x:x+w]
    cv2.imwrite('pic/apple_cut.jpg', apple_cut)

    x = 256
    orange_cut = orange_down[y:y+h, x:x+w]
    cv2.imwrite('pic/orange_cut.jpg', orange_cut)


    result = np.hstack((apple_cut, orange_cut))
    cv2.imwrite('pic/combine.jpg', result)

    for i in range(50):
        result = cv2.pyrDown(result)
        result = cv2.resize(result, (512, 512))
    cv2.imwrite('pic/pyrdown.jpg', result)

    for i in range(30):
        result = cv2.resize(result, (512, 512))
        result = cv2.pyrUp(result)
    result = cv2.resize(result, (512, 512))
    cv2.imwrite('pic/pyrup.jpg', result)

    # for i in range(10):
    #     result = cv2.pyrDown(result)
    #     result = cv2.resize(result, (512, 512))
    # cv2.imwrite('pic/result.jpg', result)

if __name__ == '__main__':
    get_apple()