import cv2
img = cv2.imread('./images/lena.jpg')
#Gaussian and Laplace's pyramids available
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr2 = cv2.pyrUp(lr2)


cv2.imshow('Orig Img', img)
cv2.imshow('pyrDown 1 Img', lr1)
cv2.imshow('pyrDown 2 Img', lr2)
cv2.imshow('pyrUp 2 Img', hr2)

#gaussian
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)

layer = gp[-1]
cv2.imshow('upper level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)
    
cv2.waitKey(0)
cv2.destroyAllWindows()