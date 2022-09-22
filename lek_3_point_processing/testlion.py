import cv2
import numpy as np

lion = cv2.imread("lion.jpg")
cv2.imshow("window",lion)
emptypng = np.zeros((lion.shape[0],lion.shape[1]),np.uint8)

print ("hello lion")
print(lion.shape)
for r in range(lion.shape[0]):
    for b in range(lion.shape[1]):
        #for g in range(lion.shape[2]):
        #    print (lion[r,b,g])
        sum = int(lion[r,b,0])+int(lion[r,b,1])+int(lion[r,b,2])
        #print(sum)
        grey = sum/3
        emptypng[r,b] = grey

cv2.imshow("empty.png", emptypng)
cv2.waitKey(0)
