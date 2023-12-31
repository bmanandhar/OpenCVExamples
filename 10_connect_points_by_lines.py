#https://www.youtube.com/watch?v=a7_dBO3EAng&ab_channel=ProgrammingKnowledge
#https://www.youtube.com/watch?v=a7_dBO3EAng&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=10&ab_channel=ProgrammingKnowledge
import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        #circle arguments: (image-data, (coordinates x and y), thickness, (3 color channels), color filling -1)
        cv2.circle(img, (x, y), 3, (0,0,255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255,0,0), 5)
        cv2.imshow('image', img)

points = []

img = np.zeros((512,512,3), np.uint8)
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event,)
cv2.waitKey(0)
cv2.destroyAllWindows()