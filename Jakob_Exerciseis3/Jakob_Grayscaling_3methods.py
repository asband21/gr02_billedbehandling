import cv2
import numpy as np
Image = cv2.imread("lion.jpg")
cv2_gray = cv2.imread("lion.jpg",cv2.IMREAD_GRAYSCALE)
nested_loop = np.zeros((Image.shape[0], Image.shape[1]),np.uint8)
matrix_multi = np.zeros((Image.shape[0], Image.shape[1]), dtype=np.uint8)
# Nested for-loop
for row in range(Image.shape[0]):
    for pixel in range(Image.shape[1]):
        for type_color in range(3):
            color = Image[row,pixel, type_color]
            nested_loop[row,pixel] = nested_loop[row,pixel] + int(color/3)

# Matrix multiplication
for color in range(3):
    matrix_multi[:,:] = np.add(matrix_multi[:,:], Image[:,:,color]/3)

cv2.imshow("Nested for-loop", nested_loop)
cv2.imshow("Matrix multip",matrix_multi)
cv2.imshow("cv2_grayscaling",cv2_gray)
cv2.waitKey(0)
