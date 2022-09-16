import cv2
import numpy as np
Image =cv2.imread("letter.png",cv2.IMREAD_GRAYSCALE)
output =np.zeros((Image.shape[0],Image.shape[1],3),dtype=Image.dtype)
#output = np.add(output,255)
def RGB_CONV(Image):
    for row in range(Image.shape[0]):
        for value in range(Image.shape[1]):
            if (row%2)==0:
                if (value%2)==0:
                    output[row,value,0] = Image[row,value]
                    blue_array=[row,value]
                    print(f"blue array {blue_array}")
                else:
                    output[row,value,1] = Image[row,value]
                    green_array = [row, value]
                    print(f"Green array {green_array}")
            else:
                if (value%2)==0:
                    output[row,value,1] = Image[row,value]
                    green_array = [row, value]
                    print(f"blue array {green_array}")
                else:
                    output[row,value,2] = Image[row,value]
                    red_array = [row, value]
                    print(f" red array {red_array}")


# array[i]=output[row,value]
def demosaicing(Image,output):
   for row in range(output.shape[0]-2):
        for pixsel in range(output.shape[1]-2):
            print(output[row,pixsel],output[row,pixsel+1],output[row, pixsel + 2])
            print(output[row+1,pixsel],output[row+ 1,pixsel+1],output[row + 1, pixsel+2])
            print(output[row+2,pixsel],output[row+2,pixsel+1],output[row+2,pixsel+2])
            print(".......")

def Show_Case(Image,output):
    cv2.imshow("Input",Image)
    cv2.imshow("Output",output)
    cv2.waitKey(0)

RGB_CONV(Image)
#demosaicing(Image,output)
#Show_Case(Image,output)