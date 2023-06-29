#https://www.youtube.com/watch?v=F9TZb0XBow0&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=30&ab_channel=ProgrammingKnowledge

import numpy as np; import cv2 as cv
import matplotlib.pyplot as plt
# img = np.zeros((200, 200), np.uint8)
# cv.imshow('img', img)
# plt.hist(img.ravel(), 256, [0, 256])
#when there is no white rectangle img has pixel valu zero, distribution pixels 200x200=40000
#add white rectangle
# img_half_white = cv.rectangle(img, (0, 100), (200, 200), (255), -1)
# cv.imshow('img_half_white', img_half_white)

#now add one more white rectangle in the black rectangle
# img_gray_added = cv.rectangle(img_half_white, (0, 50), (100, 100), (127), -1)
# cv.imshow('img_gray_added', img_gray_added)
# plt.hist(img.ravel(), 256, [0, 256])

#now, let's experiment with 'lena.jpg'

# lena = cv.imread('./images/lena.jpg') #grayscale
# b, g, r = cv.split(lena)
# cv.imshow('b', b)
# cv.imshow('g', g)
# cv.imshow('r', r)
# cv.imshow('lena', lena)

# cv.imshow('lena', lena)
# plt.hist(b.ravel(), 256, [0, 256])
# plt.hist(g.ravel(), 256, [0, 256])
# plt.hist(r.ravel(), 256, [0, 256])
# plt.hist(lena.ravel(), 256, [0, 256])

#calcHist
lena_gray = cv.imread('./images/lena.jpg', 0)
hist = cv.calcHist([lena_gray], [0], None, [256], [0, 256])
plt.plot(hist)

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

