#https://www.youtube.com/watch?v=eX7wXfNLFDw&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=18&ab_channel=ProgrammingKnowledge

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('./images/lena.jpg')
cv.imshow('Image-cv2.imshow(), RBG', img)

#opencv reads image in 'b-g-r' format
#matplotlib reads image in 'r-b-g' format
img1 = cv.cvtColor(img, cv.COLOR_BGR2RGB)

fig = plt.figure(figsize=(7, 3))
r, c = 1, 2 #(1 row, 2 cols)

fig.add_subplot(r, c, 1)
plt.imshow(img)
plt.axis('off')
plt.title('img: RGB')

fig.add_subplot(r, c, 2)
plt.imshow(img1)
plt.axis('off')
plt.title('img1: BGR2RGB')
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
