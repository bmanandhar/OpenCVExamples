#https://www.youtube.com/watch?v=V1aMDD5583k&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=6&ab_channel=ProgrammingKnowledge

import numpy as np
import cv2

# img = cv2.imread('lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8) #width, height, np-data
#st line
# image-data, start-pt, end-pt, color-bgr, thickness
img = cv2.line(img, (0,0), (255,255), (147,96,44), 10)
#arrow line
img = cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 5)

#rectangle
# image-data, top-vertex, low-vertx, color-bgr, thickness
img = cv2.rectangle(img, (384,0), (510,128), (0,0,255), 5)
img = cv2.rectangle(img, (0,265), (200,355), (0,255,255), -1)

#circle
img = cv2.circle(img, (447, 64), 64, (0,255,0), 2)
img = cv2.circle(img, (255,55), 50, (255,255,255), )
#text
#image-data, text, start-pt, font-face, font-size, color, thickness, line-type
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10,500), font, 4, (255,255,255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
