import cv2
import numpy as np

img = np.zeros((250, 500, 3), np.uint8)

img = cv2.rectangle(img, (250,0), (500,500), (255,255,255), -1)

cv2.imwrite('./images/image_1.png', img)
cv2.imshow('img', img)


cv2.waitKey(0)
cv2.destroyAllWindows()