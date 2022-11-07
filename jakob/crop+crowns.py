import numpy as np 
import cv2 
input = cv2.imread("picture/9.jpg")
output = np.zeros(input.shape,dtype=input.dtype)
input_gray = cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)
template = cv2.imread("crown.JPG",0)
w, h = template.shape[: : -1]
res= cv2.matchTemplate(input_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.44# it uses procenst, therefor 0.8 = 80%
loc = np.where(res >= threshold)
for count in range(2,3):
    for kernel_row in range(count*100,(count*100)+100):
        for count_in in range(2,3):
            for kernel_pixel in range(count_in*100,(count_in*100)+100):
                output[kernel_row,kernel_pixel] = input[kernel_row,kernel_pixel]

for pt in zip(*loc[::-1]):
    cv2.rectangle(input, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow("input", input)
#cv2.imshow("template",template)
#cv2.imshow("input_gray", input_gray)
#cv2.imshow("output", output)
cv2.waitKey(0)



