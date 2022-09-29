import cv2 as cv
import numpy as np

def fave2graa(img):
    tal = 100000000000
    ud = np.zeros((img.shape[0],img.shape[1]),np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            tal = 0
            for k in range(3):
                tal = tal + img[i,j,k]
            ud[i,j] = int(tal/3)
    return ud           

img = cv.imread("./lion.jpg")
min_graa = fave2graa(img)
opencv_graa = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("lion",img)
cv.imshow("opencv_graa",opencv_graa)
cv.imshow("min_graa",min_graa)

cv.waitKey(0)
