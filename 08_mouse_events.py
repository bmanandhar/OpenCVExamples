#https://www.youtube.com/watch?v=rrh-4NtuK-w&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=9&ab_channel=ProgrammingKnowledge
import cv2
import numpy as np
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print('(', x, ', ', y, ')')
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = '(' + str(x) + ', ' + str(y) + ')'
        cv2.putText(img, strXY, (x,y), font, 0.5, (255,255,0), 2)
        cv2.imshow('Image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = '(' + str(blue) + ', ' + str(green) + ', ' + str(red) + ')'
        cv2.putText(img, strBGR, (x,y), font, 0.5, (255,0,255), 2)
        cv2.imshow('Image', img)

# img = np.zeros((512,512,3), np.uint8)
# img = cv2.imread('./lena.jpg')
img = cv2.imread('./images/messi5.jpg')
cv2.imshow('Image', img)

cv2.setMouseCallback('Image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows