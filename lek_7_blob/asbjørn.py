import cv2 as cv
import numpy as np
import sys
sys.setrecursionlimit(10000)


def gras(img,x,y,d,farve_brant):
    for i in farve_brant:
        if np.array_equal(img[x,y], i):
            return 0
    if np.array_equal(d, np.zeros(3)):
        d = np.random.random_integers(255,size=(3)) 
        farve_brant.append(d)
    img[x,y] = d
    li = [[1,0],[-1,0],[0,-1],[0,1]]
    for i in li:
        if -1 < x+i[0] < img.shape[0] and -1 < y+i[1] < img.shape[0]:
            gras(img, x+i[0], y+i[1], img[x,y], farve_brant )
    return 1

img = cv.imread("./shapes.png")
blobber = 0
farve_brant = [np.random.random_integers(255,size=(3))*0]
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        blobber = blobber + gras(img,i,j,np.array([0,0,0]),farve_brant)
print(f"antal blober:{blobber}")
cv.imshow("img",img)
cv.waitKey(0)
