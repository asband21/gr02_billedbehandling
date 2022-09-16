import cv2
import numpy as np

#Image = cv2.imread("letter.png",cv2.IMREAD_GRAYSCALE)
Image = cv2.imread("tinypic.png",cv2.IMREAD_GRAYSCALE)
output =np.zeros((Image.shape[0],Image.shape[1],3),dtype=Image.dtype)
Image =np.append(Image, np.zeros((Image.shape[0],3)),axis=1)
Image =np.append(Image, np.zeros((3,Image.shape[1])),axis=0)
print(f"{Image.shape[0]} {Image.shape[1]}")
#output = np.add(output,255)
def RGB_CONV(Image):
    for row in range(Image.shape[0]-3):
        for value in range(Image.shape[1]-3):
            if (row % 2) == 0:
                if (value % 2) == 0:
                    output[row, value, 0] = Image[row, value]
                    #for row2 in range(row, row + 3):
                      #  for pixel in range(value, value+3):
                           # blue_array = output[row, value, 0]
                            #print(f"Blue array {blue_array} in {[row, value]}")
# Try to inceret the values of the blue pixels from output into a 2d blue_array
                else:
                    output[row, value, 1] = Image[row, value]
                    green_array = np.zeros((3, 3))
                    for row2 in range(row, row + 3):
                        for pixel in range(value, value + 3):
                            print(f"x{row}y{value}")
                            if True: #outpt[row, value, 1] != 0:
                                print(f"green_array[{row2}-{row}, {pixel}-{value}] = output[{row2}, {pixel}, 1]")
                                green_array[row2-row, pixel-value] = Image[row2, pixel]
                                print(output[row, value, 1])
                                print(f"Green array{green_array} in {[row2, pixel]}")

            else:
                if (value % 2) == 0:
                    output[row, value, 1] = Image[row,value]
                    #for row2 in range(row, row + 3):
                       # for pixel in range(value, value + 3):
                           # if output[row, value, 1] != 0:
                               # green_array = output[row2, pixel, 1]
                                #print(f"Green array {green_array} in {[row, value]}")


                else:
                    output[row, value, 2] = Image[row, value]
                    #for row2 in range(row, row + 3):
                        #for pixel in range(value, value + 3):
                           # if output[row, value, 2] != 0:
                               # red_array = output[row2, pixel, 2]
                                #print(f"Red array {red_array} in {[row, value]}")




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
