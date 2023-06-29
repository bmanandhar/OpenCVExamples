import cv2; import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/lena.jpg', cv2.IMREAD_GRAYSCALE)
#5 different steps
canny = cv2.Canny(img, 100, 200) #th1, th2

titles = ['image', 'canny']
images = [img, canny]
for i in range(len(titles)):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])

plt.show()