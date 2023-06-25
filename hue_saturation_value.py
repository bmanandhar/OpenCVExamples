#https://www.youtube.com/watch?v=3D7O_kZi8-o&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=14&ab_channel=ProgrammingKnowledge

import numpy as np
import cv2

# Hue: corrsponds to the color components(base pigment),
# by selecting a range of Hue, we can select any color (0-360).
# Saturation: is the amount of color
# (depth of pigment, dominance of Hue (0-100%)
# Value is basically the brightness of the color(0-100%)

def nothing(x):
    pass

#video captures
cap = cv2.VideoCapture(0)

cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)



while True:
    # frame = cv2.imread('./images/smarties.png')
    _, frame = cap.read(pwd)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #detecting only blue color
    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')

    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking')

    l_b = np.array([l_h, l_s, l_v]) #lower boundation
    u_b = np.array([u_h, u_s, u_v]) #upper boundation

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Res', res)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()