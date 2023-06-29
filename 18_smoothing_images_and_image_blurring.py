#https://www.youtube.com/watch?v=u3poUhCxx4k&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=20&ab_channel=ProgrammingKnowledge
import cv2; import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('./images/opencv-logo.png')
# img = cv2.imread('./images/Halftone_Gaussian_Blur.jpg')
# img = cv2.imread('./images/water.png')
img = cv2.imread('./images/lena.jpg')


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#homogenous filter

'''
k is a matrix
k = 1/(width of kernel)*(height of kernel)
'''
kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
# 5 is kernel size, it has to be an odd umber except 1
#gaussian blur
gblur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75 )

titles = ['image', '2D Convolution', 'blur', 'gaussian blur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(len(titles)):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

