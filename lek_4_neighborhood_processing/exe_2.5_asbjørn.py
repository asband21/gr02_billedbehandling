import cv2 as cv
import numpy as np


def kernel(img,ker):
    tal = 100000000000
    sum_tal = 100000000000
    sum_tal = int(ker.sum())
    rx = int((ker.shape[0]-1)/2)
    ry = int((ker.shape[1]-1)/2)
    print(sum_tal)
    ud = np.zeros((img.shape[0],img.shape[1],img.shape[2]),np.uint8)
    for x in range(rx,img.shape[0]-rx):
        for y in range(ry,img.shape[1]-ry):
            for k in range(img.shape[2]):
                tal = 0
                for i in range(-rx, rx+1):
                    for j in range(-ry ,ry+1):
                        tal = tal+ ker[i,j]*img[x+i,y+j,k]
                ud[x,y,k] = int(tal/sum_tal)
    return ud           

#ker_mid = np.array([[1,1,1],[1,1,1],[1,1,1]])
ker_mid = np.zeros((5,5))+1

img = cv.imread("./lion.jpg")
min_graa = kernel(img,ker_mid)
opencv_graa = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("lion",img)
cv.imshow("opencv_graa",opencv_graa)
cv.imshow("min_graa",min_graa)

cv.waitKey(0)
