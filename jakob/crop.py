import numpy as np 
import cv2 
input = cv2.imread("picture/4.jpg")
output = np.zeros(input.shape,dtype=input.dtype)
for count in range(5):
    for kernel_row in range(count*100,(count*100)+100):
        for count_in in range(5):
            for kernel_pixel in range(count_in*100,(count_in*100)+100):
                output[kernel_row,kernel_pixel] = input[kernel_row,kernel_pixel]
cv2.imshow("input", input)
cv2.imshow("output", output)
cv2.waitKey(0)



