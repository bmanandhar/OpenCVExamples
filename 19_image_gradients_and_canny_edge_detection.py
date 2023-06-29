import cv2; import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/messi5.jpg', cv2.IMREAD_GRAYSCALE)
#laplacian image transformation - gradient
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) #1-x dir, 0-y dir
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1) #in Y dir

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

#combine all
sobelCombined = cv2.bitwise_or(sobelX, sobelY)
canny = cv2.Canny(img, 100, 200) #th1, th2

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined', 'canny']
images = [img, lap, sobelX, sobelY, sobelCombined, canny]
for i in range(len(titles)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i]), plt.xticks([]), plt.yticks([])

plt.show()