import cv2
import numpy as np


Input_image = cv2.imread("lion.jpg")
Grayscaling_image = cv2.imread("lion.jpg", cv2.IMREAD_GRAYSCALE)
Loop_image = np.zeros((Input_image.shape[0], Input_image.shape[1]), np.uint8)
Matrix_image = np.zeros((Input_image.shape[0], Input_image.shape[1]), np.uint8)



for row in range(Input_image.shape[0]):
    for pixel in range(Input_image.shape[1]):
        blue = Input_image[row, pixel, 0]
        green = Input_image[row, pixel, 1]
        red = Input_image[row, pixel, 2]

        Loop_image[row, pixel] = int(((blue/3)+(green/3)+(red/3)))


for i in range(3):
    Matrix_image[:,:] = np.add(Matrix_image[:,:], Input_image[:,:,i]/3)

cv2.imshow("Input image", Input_image)
cv2.imshow("Looping", Loop_image)
cv2.imshow("matrix", Matrix_image)
cv2.imshow("grayscaling", Grayscaling_image)
cv2.waitKey(0)