import cv2
import numpy as np

apple = cv2.imread('apple_pic/apple.jpg')
orange = cv2.imread('apple_pic/orange.jpg')

apple_copy = apple.copy()

# Guassian Pyramids for apple
apple_guassian = [apple_copy]

for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    apple_guassian.append(apple_copy)
    

# Guassian Pyramids for apple
orange_copy = orange.copy()
orange_gaussian = [orange_copy]

for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    orange_gaussian.append(orange_copy)

# Laplacian Pyramids for apple
apple_copy = apple_guassian[5]
apple_laplacian = [apple_copy]

for i in range (5,0,-1):
    gaussian_extended = cv2.pyrUp(apple_guassian[i])
    
    laplacian = cv2.subtract(apple_guassian[i-1],gaussian_extended)
    apple_laplacian.append(laplacian)
    
# Laplacian Pyramids for orange
orange_copy = orange_gaussian[5]
orange_laplacian = [orange_copy]

for i in range (5,0,-1):
    gaussian_extended = cv2.pyrUp(orange_gaussian[i])
    
    laplacian = cv2.subtract(orange_gaussian[i-1],gaussian_extended)
    orange_laplacian.append(laplacian)
    
# join the left half of apple and right half of orange in each levels of Laplacian Pyramids
apple_orange_pyramid = []
n = 0
for apple_lp,orange_lp in zip(apple_laplacian,orange_laplacian):
    n += 1
    cols,rows,ch = apple_lp.shape
    laplacian = np.hstack((apple_lp[:,0:int(cols/2)],orange_lp[:,int(cols/2):]))
    apple_orange_pyramid.append(laplacian)
    
#reconstrut image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i],apple_orange_reconstruct)
    
    
cv2.imwrite("apple_pic/apple.jpg",apple)
cv2.imwrite("apple_pic/orange.jpg",orange)
cv2.imwrite("apple_pic/apple_orange_reconstruct.jpg",apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()