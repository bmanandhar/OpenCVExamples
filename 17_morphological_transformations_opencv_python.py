#https://www.youtube.com/watch?v=xSzsD4kXhRw&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=19&ab_channel=ProgrammingKnowledge

import cv2; import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('./images/smarties.png', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('./images/j.png', cv2.IMREAD_GRAYSCALE)


#morphological tranformation are performed normally on binary images
#hence, mask is used
# _, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)
#we see some black dots in mask-image that we want to remove

kernal = np.ones((5, 5), np.uint8) #small square of size 2x2
#morphological transformations
# dilation = cv2.dilate(mask, kernal, iterations=2)
# erosion = cv2.erode(mask, kernal, iterations=1)
# opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
# gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
# tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)
# closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

#j.png is already a mask image
dilation = cv2.dilate(img, kernal, iterations=2)
erosion = cv2.erode(img, kernal, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernal)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernal)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'gradient', 'tophat', 'closing']
images = [img, img, dilation, erosion, opening, gradient, tophat, closing]

for i in range(len(titles)):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()