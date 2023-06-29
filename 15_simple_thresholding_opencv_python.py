#https://www.youtube.com/watch?v=CdltAssTMs8&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=15&ab_channel=ProgrammingKnowledge

import cv2 as cv
import numpy as np

# the image that is being used here has a gradient
# that is lower, 0 on the lhs and 255 on rhs.

(0 + 255) // 2 == 127
img = cv.imread('./images/gradient.png', 0)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

cv.imshow('Image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)
cv.imshow('th4', th4)
cv.imshow('th5', th5)

# use of matplotlib library to show multiple images in a frame
titles = ['Orig image-img', 'BINARY-th1', 'BINARY_INV-th2', 'TRUNC-th3', 'TOZERO-th4', 'TOZERO_INV-th5']
images = [img, th1, th2, th3, th4, th5]

from matplotlib import pyplot as plt

for i in range(len(images)):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()