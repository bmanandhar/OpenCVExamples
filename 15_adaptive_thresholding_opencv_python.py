#https://www.youtube.com/watch?v=Zf1F4cz8GHU&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=17&ab_channel=ProgrammingKnowledge

import cv2 as cv
import numpy as np
#the image that is being used here has a gradient
# that is lower, 0 on the lhs and 255 on rhs.

(0+255)//2 == 127
img = cv.imread('./images/sudoku.png', 0)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)


cv.imshow('Image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)


cv.waitKey(0)
cv.destroyAllWindows()