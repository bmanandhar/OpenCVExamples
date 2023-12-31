import numpy as np
import cv2

def nothing(x):
    print(x)

img = cv2.imread('./images/lena.jpg')

cv2.namedWindow('Image')

cv2.createTrackbar('CP', 'Image', 10, 400, nothing)

#toggle between color to grayscale
switch = 'color/gray'
cv2.createTrackbar(switch, 'Image', 0, 1, nothing)

while 1:
    img = cv2.imread('./images/lena.jpg')
    pos = cv2.getTrackbarPos('CP', 'Image')
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(pos), (50, 150), font, 6, (0, 0, 255), 10)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    s = cv2.getTrackbarPos(switch, 'Image')
    if s != 1:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.imshow('Image', img)

cv2.destroyAllWindows()