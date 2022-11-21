import numpy as np 
import cv2
input = cv2.imread("picture/9.jpg")
where_crown = cv2.imread("picture/9.jpg")
where_crown_array = np.zeros([5,5])
crop = np.zeros(input.shape, dtype=input.dtype)
input_gray = cv2.cvtColor(where_crown, cv2.COLOR_BGR2GRAY)
template = cv2.imread("krone_master.png", 0)
w, h = template.shape[: : -1]
res1 = cv2.matchTemplate(input_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.80 #it uses procenst, therefor 0.8 = 80%
loc = np.where(res1 >= threshold)

for count in range(0, 5):  # divied the pictues into 5x5 crops
    for kernel_row in range(count*100, (count*100)+100): #takes the size of one crop x-axes
        for count_in in range(0, 5): #divied the pictues into 5x5 crops
            for kernel_pixel in range(count_in*100, (count_in*100)+100): #takes the size of one crop y-axes
                for pt in zip(*loc[::-1]):
                    if (pt[0]) == kernel_pixel and (pt[1]) == kernel_row: #matching the postion of template matching with every pixel in one "crop"
                        where_crown_array[count, count_in] = 1
                if 1 == where_crown_array[count, count_in]: #crops foto, based on where_crown_array
                    crop[kernel_row, kernel_pixel] = input[kernel_row, kernel_pixel]

for pt in zip(*loc[::-1]): #Places a yellow rectanle on the template match
    cv2.rectangle(where_crown, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 1)


cv2.imshow("input", input)
cv2.imshow("crown",where_crown)
#cv2.imshow("template",template)
#cv2.imshow("input_gray", input_gray)
cv2.imshow("Crop", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()



