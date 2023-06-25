import numpy as np
import cv2

img = cv2.imread('./images/messi5.jpg')
img2 = cv2.imread('./images/opencv-logo.png')

print(f'{img.shape= }') #(rows, cols, channels)
print(f'{img.size= }')  #tot num of pixels
print(f'{img.dtype= }') #Image datatype

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

#Region of interest (roi)
#let's work with the ball in image as 'roi'
#to know the location where the ball is, use 'mouse_events'
ball = img[280:340, 330:390]
#we want to place the ball at some other place (273:333, 100:160)
img[273:333, 100:160] = ball
#resize to fit in
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, 0.9, img2, 0.1, 0)

cv2.imshow('Messi', dst)

# cv2.imshow('Messi', img)

cv2.waitKey(0)
cv2.destroyAllWindows()