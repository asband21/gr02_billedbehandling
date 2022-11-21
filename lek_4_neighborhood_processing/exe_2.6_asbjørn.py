import cv2 as cv
import numpy as np


def kernel(img,ker):
    tal = 1000000.00000
    sum_tal = 1000000.00000
    sum_tal = ker.sum()/(ker.shape[0]*ker.shape[1])
    rx = int((ker.shape[0]-1)/2)
    ry = int((ker.shape[1]-1)/2)
    print(sum_tal)
    ud = np.zeros((img.shape[0],img.shape[1]),np.uint8)
    for x in range(rx,img.shape[0]-rx):
        print(x)
        for y in range(ry,img.shape[1]-ry):
            tal = 0
            for i in range(-rx, rx+1):
                for j in range(-ry ,ry+1):
                    tal = tal + ker[i,j]*img[x+i,y+j]*sum_tal
            ud[x,y] = int(tal)
    return ud           

ker_mid = cv.imread("./herte_templed.png", cv.IMREAD_GRAYSCALE)
img = cv.imread("./neon-text.png", cv.IMREAD_GRAYSCALE)
cv.imshow("neo",img)
cv.imshow("tem",ker_mid)
cv.waitKey(0);
img = kernel(img, np.zeros((5,5))+1)
min_graa = kernel(img,ker_mid)

cv.imshow("lion",img)
cv.imshow("min_graa",min_graa)

cv.waitKey(0)
