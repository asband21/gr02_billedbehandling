import cv2
import numpy as np
import math
dots = cv2.imread("/home/alex/Hentet/dots.gif")
cv2.imshow("window",dots)
emptypng = np.zeros( ( dots.shape[0], dots.shape[1], dots.shape[2] ), np.uint8)


#kernel som skal kunne ændres nemt
#mean filter
#førsn skal pixels plusses og divideres med antal pixels i kerne
kernel =np.array([[1,0,1],[0,1,0],[1,0,1]])

for j in range(0,3):
    for k in range(0,3):
        print(kernel[j,k])
n = 0
m = 3
for t in range(dots.shape[0]-3):
	for f in range(dots.shape[1]-3):
		for y in range(t,t+kernel.shape[0]):
			for x in range(f,f+kernel.shape[1]):
				print(lion[y,x,:])
		print("------")
		n = n + 1 
		m = m + 1 



print ("hello lion")
print(lion.shape)
for x  in range(dots.shape[0]):
    for y in range(dots.shape[1]):
        for z in range(dots.shape[2]):
           # print (dots[x,y,z])
            r = (dots[x,y,0])
            b = (dots[x,y,1])
            g = (dots[x,y,2])
            c = [r,b,g]
            emptypng[x,y,z] = dots[x,y,z]
cv2.imshow("empty.png", emptypng)
cv2.waitKey(0)

