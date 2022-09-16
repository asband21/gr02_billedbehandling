import cv2
import numpy as np
Image =cv2.imread("tinypic.png",cv2.IMREAD_GRAYSCALE)
output =np.zeros((Image.shape[0],Image.shape[1],3),dtype=Image.dtype)
#output = np.add(output,255)
def RGB_CONV(Image):
    for row in range(Image.shape[0]):
        for value in range(Image.shape[1]):
            if (row % 2) == 0:
                if (value % 2) == 0:
                    output[row, value, 0] = Image[row, value]
                    blue_array = np.zeros((3, 3))
                    if output[row, value, 0] != 0:
                        for row2 in range(row, row + 3):
                            for pixel in range(value, value + 3):

                                blue_array[row2 - row, pixel - value] = output[row2 - row, pixel - value, 0]
                                # print(f"Green array: {green_array} in {[ pixel-value,row2-row]}")
                                if blue_array[row2-row, pixel-value] != 0:
                                    a=1
                                    a+= a+1

                                    print(f"blue count is {a}")
                            print(f" blue{blue_array}")
                else:
                    output[row, value, 1] = Image[row, value]
                    green_array = np.zeros((3, 3))
                    if output[row, value, 1] != 0:
                        for row2 in range(row, row + 3):
                            for pixel in range(value, value + 3):
                                green_array[row2-row, pixel-value] = output[row2-row, pixel-value, 1]
                                #print(f"Green array: {green_array} in {[ pixel-value,row2-row]}")
                        print(f" green{green_array}")
            else:
                if (value % 2) == 0:
                    output[row, value, 1] = Image[row, value]
                    green_array = np.zeros((3, 3))
                    if output[row, value, 1] != 0:
                        for row2 in range(row, row + 3):
                            for pixel in range(value, value + 3):
                                green_array[row2 - row, pixel - value] = output[row2 - row, pixel - value, 1]
                                #print(f"Green array: {green_array} in {[ pixel-value,row2-row]}")
                                if green_array[row2-row, pixel-value]!= 0:
                                    a = 0
                                    a += a + 1
                                    print(f"green count is {a}")
                                print(f" green{green_array}")
                else:
                    output[row, value, 2] = Image[row, value]
                    red_array = np.zeros((3, 3))
                    if output[row, value, 2] != 0:
                        for row2 in range(row, row + 3):
                            for pixel in range(value, value + 3):
                                red_array[row2 - row, pixel - value] = output[row2 - row, pixel - value, 2]
                                # print(f"Green array: {green_array} in {[ pixel-value,row2-row]}")
                    print(f"red{red_array}")




# array[i]=output[row,value]
def demosaicing(Image,output):
   for row in range(output.shape[0]-2):
        for pixsel in range(output.shape[1]-2):
            print(output[row,pixsel],output[row,pixsel+1],output[row, pixsel + 2])
            print(output[row+1,pixsel],output[row+ 1,pixsel+1],output[row + 1, pixsel+2])
            print(output[row+2,pixsel],output[row+2,pixsel+1],output[row+2,pixsel+2])
            print(".......")
def Show_Case(Image,output):
    cv2.imshow("Input", Image)
    cv2.imshow("Output", output)
    cv2.waitKey(0)

RGB_CONV(Image)
#demosaicing(Image,output)
Show_Case(Image, output)