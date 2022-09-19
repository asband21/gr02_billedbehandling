import cv2
import numpy as np
Image = cv2.imread("letter.png ", cv2.IMREAD_GRAYSCALE)
Image2 = cv2.imread("letter.png ")
output = np.zeros((Image.shape[0], Image.shape[1], 3), dtype=Image.dtype)
#output = np.add(output,255)
g = 0
b = 0
r = 0
def Color_Counter(rgb_array, color_count):
    for check_x in range(3):
        for check_y in range(3):
            if rgb_array[check_x, check_y] != 0:
                color_count = color_count + 1
    return color_count
def Average_calculator(color_array, color_count):
    sum_of_color = (sum(sum(color_array)))
    average = sum_of_color/color_count
    #average = np.median(color_array)
    return average

def RGB_CONV(Image):
    blue_array = np.zeros((3, 3))
    green_array = np.zeros((3, 3))
    red_array = np.zeros((3, 3))
    for row in range(Image.shape[0]):
        for value in range(Image.shape[1]):
            if (row % 2) == 0 and (value % 2) == 0:
                output[row, value, 0] = Image[row, value]
                for row2 in range(row, row + 3):
                    for pixel in range(value, value + 3):
                        blue_array[row2 - row, pixel - value] = output[row2 - row, pixel - value, 0]
                for row3 in range(blue_array.shape[0]):
                    for pixel3 in range(blue_array.shape[1]):
                        if (row3 % 2) == 0 and (pixel3 % 2) == 0 and output[row3, pixel3, 0] != 0:
                            output[row3, pixel3, 0] = Average_calculator(blue_array, Color_Counter(blue_array, b))

            elif (row % 2) == 0 and (value % 2) != 0 or (row % 2) != 0 and (value % 2) == 0:
                output[row, value, 1] = Image[row, value]
                for row2 in range(row, row + 3):
                    for pixel in range(value, value + 3):
                        green_array[row2-row, pixel-value] = output[row2-row, pixel-value, 1]
                for row3 in range(green_array.shape[0]):
                    for pixel3 in range(green_array.shape[1]):
                        if (row3 % 2) == 0 and (pixel3 % 2) != 0 and output[row3, pixel3, 1] != 0 or (row3 % 2) != 0 and (pixel3 % 2) == 0 and output[row3, pixel3, 1] != 0:
                            output[row3, pixel3, 1] = Average_calculator(green_array, Color_Counter(green_array, g))

            elif (row % 2) != 0 and (value % 2) != 0:
                output[row, value, 2] = Image[row, value]
                for row2 in range(row, row + 3):
                    for pixel in range(value, value + 3):
                        red_array[row2 - row, pixel - value] = output[row2 - row, pixel - value, 2]
                for row3 in range(red_array.shape[0]):
                    for pixel3 in range(red_array.shape[1]):
                        if (row3 % 2) == 0 and (pixel3 % 2) == 0 and output[row3, pixel3, 2] != 0:
                            output[row3, pixel3, 0] = Average_calculator(red_array, Color_Counter(red_array, r))
def Show_Case(Image, output, Image2):
    cv2.imshow("Input_GRAY-SCALE", Image)
    cv2.imshow("Input_RGB", Image2)
    cv2.imshow("Output", output)
    cv2.waitKey(0)

#demosaicing
RGB_CONV(Image)
Show_Case(Image, output, Image2)