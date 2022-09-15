import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import pdb

for i in range(1,75,1):
    img = cv.imread(str(i) + ".jpg")
    sm_img = np.full((100, 100, 3), (0,0,0), dtype=np.uint8)
    hsv_img = np.full((100, 100, 3), (0,0,0), dtype=np.uint8)
    tel = 1
    for j in range(0,500,100):
        for k in range(0,500,100):
            sit = str(i)+"/"+str(tel) + "/"
            f = open(sit+"h_mono.csv","w")
            for x in range(100):
                for y in range(100):
                    for z in range(3):
                        sm_img[x,y,z] = img[j+x,k+y,z]
            #pdb.set_trace()
            hsv_img = cv.cvtColor(sm_img, cv.COLOR_BGR2HSV)
            if(False  == cv.imwrite(sit+"normal.png",sm_img)):
                print("pik")
            cv.imwrite(sit+"hsv.png",hsv_img)
            cv.imwrite(sit+"h_mono.png",sm_img[:,:,0])
            for x in range(100):
                for y in range(100):
                    f.write(str(hsv_img[x,y,0])+"\n")
            f.close()
            tel = tel + 1
