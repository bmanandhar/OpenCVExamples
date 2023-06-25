import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue, green, red = img[x, y, 0], img[x, y, 1], img[x, y, 2]
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        myColorImage = np.zeros((512,512,3), np.uint8)

        myColorImage[:] = [blue, green, red]

        cv2.imshow('Color', myColorImage)

img = cv2.imread('./images/lena.jpg')
cv2.imshow('Image', img)
points = []
cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
