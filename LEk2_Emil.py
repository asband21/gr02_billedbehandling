import cv2
import numpy as np

input_image = cv2.imread("Letter.png", cv2.IMREAD_GRAYSCALE)
output_image = np.zeros((input_image.shape[0], input_image.shape[1], 3), dtype=input_image.dtype)

for row in range(output_image.shape[0]):
    for pixel in range(output_image.shape[1]):
        if (row % 2) == 0:
            if (pixel % 2) == 0:
                output_image[row, pixel, 0] = input_image[row, pixel]
            else:
                output_image[row, pixel, 1] = input_image[row, pixel]

        if (row % 2) == 1:
            if (pixel % 2) == 1:
                output_image[row, pixel, 2] = input_image[row, pixel]
            else:
                output_image[row, pixel, 1] = input_image[row, pixel]


#red = input_image[:, :, 2]
#green = input_image[:, :, 1]
#blue = input_image[:, :, 0]

cv2.imshow("input image", input_image)
#cv2.imshow("Red channel", red)
#cv2.imshow("green channel", green)
#cv2.imshow("blue channel", blue)
cv2.imshow("output image", output_image)
cv2.waitKey(0)
