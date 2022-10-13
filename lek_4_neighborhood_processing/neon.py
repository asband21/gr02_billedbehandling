import cv2
import numpy as np
import math
lion = cv2.imread("lion.jpg")
cv2.imshow("window",lion)
emptypng = np.zeros( ( lion.shape[0], lion.shape[1], lion.shape[2] ), np.uint8)

mean_kernel = np.ones((9.9))
output = np.zeroes(mean_kernel.shape[0]+1,mean_kernel.shape[1]+1)
print(mean_kernel)

cv.imshow("output",output)

#kernel som skal kunne ændres nemt
#mean filter
#førsn skal pixels plusses og divideres med antal pixels i kerne


def convolve(image,kernel):
	for y  in range(output.shape[0]):
		for x in range(output.shape.shape[1]):
			slice = img[y:y+kernel_size,x:x+kernel_size]
			output[x,y] = np.sum(slice*mean_kernel)/np.sum(mean_kernel)
				




gaussian_kernel = np.ones((11,11))
mean = convolve(img,gaussian_kernel)


cv.imshow("input", img)
cv.imshow("outpu", output)
cv.waitKey(0)


