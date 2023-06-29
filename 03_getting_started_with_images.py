#https://github.com/opencv/opencv/tree/master/samples
# https://www.youtube.com/watch?v=44xdiWLm4Xo&ab_channel=ProgrammingKnowledge

#cv2.imread('lena.jpg', 1) #colored image
#cv2.imread('lena.jpg', 0) #grayscale image
#cv2.imread('lena.jpg', -1)#image with alpha channel

import cv2
img = cv2.imread('./images/lena.jpg', 1)
print(img)
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()
