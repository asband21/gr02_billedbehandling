import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import pdb

film_nu = 0 % 200 + 1  
ter_set = 0 % 34 + 1
del_film_nu = 0 % 200 + 1  
delta = 5

a = 0.4
while(1):
    print(f"\t ter_set:{ter_set:02d} \tfilm_nu:{film_nu+1:03d} \tdelta:{delta:02d}                  ",end ='\r')
    
    sti = f"./UCSD_Anomaly_Dataset.v1p2/UCSDped1/Train/Train{ter_set+1:03d}/{film_nu+1:03d}.tif"
    sti_del = f"./UCSD_Anomaly_Dataset.v1p2/UCSDped1/Train/Train{ter_set+1:03d}/{del_film_nu+1:03d}.tif"
    img = cv.imread(sti)
    del_img = cv.imread(sti_del) 
    dif_img = cv.subtract(img,del_img);
    dif_img_2 = cv.subtract(del_img,img);
    img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    del_img_gray = cv.cvtColor(del_img,cv.COLOR_BGR2GRAY)
    a_img = cv.multiply(img_gray,a) + cv.multiply(del_img_gray,(1-a))
    cv.imshow("Train",img)
    cv.imshow("a*img+(1-a)*del_img",a_img)
    cv.imshow("Train delta",del_img)
    cv.imshow("Train sub",dif_img)
    cv.imshow("Train sub_2",dif_img_2)
    k = cv.waitKey(5) & 0xFF
    if k == 110:
        film_nu = (film_nu + 1) % 200   
        del_film_nu = (film_nu +delta) % 200   
    if k == 98:
        film_nu = (film_nu - 1) % 200   
        del_film_nu = (film_nu +delta) % 200   
    if k == 103:
        ter_set = (ter_set + 1) % 34 
    if k == 104:
        ter_set = (ter_set - 1) % 34
    if k == 121:
        delta = delta +1 
        del_film_nu = (film_nu +delta) % 200   
    if k == 116:
        delta = delta - 1 
        del_film_nu = (film_nu +delta) % 200   
    if k == 27:
        #pass
        break
cv.destroyAllWindows()
