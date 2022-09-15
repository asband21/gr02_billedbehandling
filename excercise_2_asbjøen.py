import cv2 as cv
import numpy as np
import pdb
def demosaicing(img):
    size = img.shape
    farve = np.zeros((size[0],size[1],3), np.uint8)
    for i in range(size[0]):
        for j in range(size[1]):
            if (j+i) & 1:
                farve[i,j,1]=img[i,j]
            elif i & 1:
                farve[i,j,0]=img[i,j]
            else:
                farve[i,j,2]=img[i,j]
    #print(size)
    return farve

def bere_smude(img):
    size = img.shape
    for i in range(1,size[0]-1):
        for j in range(1,size[1]-1):
            for k in range(3):
                if img[i,j,k] == 0:
                    teller = 0
                    tutal = 0
                    for x in range(-1,1):
                        for y in range(-1,1):
                            if(x+y & 1):
                                teller = teller + 1 
                                tutal = tutal +img[i+x,j+y,k]
                    if teller > 1:
                        img[i,j,k] = tutal/teller 
    return img

cap = cv.VideoCapture(0)
while(1):
#if True:
    _, frame = cap.read()
    gray = cv.cvtColor(frame[400:600,400:600,:], cv.COLOR_BGR2GRAY)
    res = demosaicing(gray)
    res_galt = bere_smude(res.copy())

    cv.imshow('ind',frame)
    cv.imshow('grAA',gray)
    cv.imshow('bere',res)
    cv.imshow('bere glat',res_galt)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        #pass
        break
cv.destroyAllWindows()
