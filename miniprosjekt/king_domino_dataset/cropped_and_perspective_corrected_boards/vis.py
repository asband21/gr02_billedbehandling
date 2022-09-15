import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np
import pdb

teller = 0
bil_tel = 0
while(1):
    sti = str(bil_tel+1)+"/"+str(teller+1) + "/"
    img = cv.imread(sti +"normal.png")
    plad = cv.imread(str(bil_tel+1) +".jpg")
    hsv_mono = cv.imread(sti +"h_mono.png")
    hsv_plot = cv.imread(sti +"h_mono_plot.png")
    cv.imshow('normal',img)
    cv.imshow('plade',plad)
    cv.imshow('HSV mono',hsv_mono)
    cv.imshow('HSV plot',hsv_plot)
    k = cv.waitKey(5) & 0xFF
    if k != 255:
        print(sti)
    if k == 110:
        teller = (teller + 1 ) % 25
    if k == 98:
        teller = (teller - 1 ) % 25
    if k == 103:
        bil_tel = (bil_tel - 1 ) % 74
    if k == 104:
        bil_tel = (bil_tel + 1 ) % 74
    if k == 99:
        print("lower hsv bound")
    if k == 27:
        break
cv.destroyAllWindows()

