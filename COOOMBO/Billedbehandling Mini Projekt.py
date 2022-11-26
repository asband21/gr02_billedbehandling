import numpy as np
import cv2 as cv
import math


picture = ("4.jpg")

inputImage = cv.imread(picture)

w=3*100
h=3*100
workImage = inputImage[h:h+100,w:w+100]

outputImage = np.zeros(inputImage.shape)


def average(img, lower, upper,i):


    name = ("water", "farm", "grass", "forest", "cave", "swamp")
    threshold = cv.inRange(img, lower, upper)
    ##cv.imshow("threshold", threshold)
    cv.imshow("threshold " + name[i], threshold)
    return threshold.sum()/2560000
    ##return threshold.sum()/64000000




#define environment
def environment(image):
    hsvImage = cv.cvtColor(image, cv.COLOR_BGR2HSV_FULL)


#water = (h=[140, 160], S[200,255],v)
    avg = average(hsvImage, np.array([140, 220, 0]), np.array([160, 255, 255]));
    #avg = average(hsvImage, np.array([140, 220, 0]), np.array([160, 255, 255]));
    print("water ="+str(avg))
    if 0.3 < avg:
        print("nice")

#farm = (h=[30,40], s[220,255], v[170,210])
    avg = average(hsvImage, np.array([30, 220, 160 ]), np.array([40, 255, 210]),1);
    #avg = average(hsvImage, np.array([30, 220, 160]), np.array([40, 255, 210]));
    #print(avg)
    print("farm ="+str(avg))
    if 0.35 < avg:
        print("nice")

#grass = (h=[55,75], s[190,255], v[150,215])
    avg = average(hsvImage, np.array([40, 190, 100]), np.array([75, 255, 215]),2);
    #avg = average(hsvImage, np.array([40, 190, 100]), np.array([75, 255, 215]));
    #print(avg)
    print("grass ="+str(avg))
    if 0.15 < avg:
        print("nice")

#forest = (h=[62,90], s[118,255], v[37,80])
    avg = average(hsvImage, np.array([62, 90,37]), np.array([90, 255, 80]),3);
    #avg = average(hsvImage, np.array([62, 90, 37]), np.array([90, 255, 80]));
    #print(avg)
    print("forest ="+str(avg))
    if 0.10 < avg:
        print("nice")

#cave = (h[10,25], s[0,55], v[30,75])
    avg = average(hsvImage, np.array([150, 0, 0]), np.array([255, 124, 78]),4);
    #avg = average(hsvImage, np.array([0, 0, 0]), np.array([52, 124, 78]));
    #print(avg)
    print("cave ="+str(avg))
    if 0.10 < avg:
        print("nice")

#swamp = (h[14,39], s[90,189], v[70,165])
    avg = average(hsvImage, np.array([14, 0, 70]), np.array([39, 189, 165]),5);
    #avg = average(hsvImage, np.array([14, 90, 70]), np.array([39, 189, 165]));
    #print(avg)
    print("swamp ="+str(avg))
    if 0.30 < avg:
         print("nice")








#main=
#slice environment



#recognize crown object

#check environment

#check surrounding environment

environment(workImage)

#cv.imshow("RGB", inputImage)
cv.imshow("out", workImage)
cv.waitKey(0)