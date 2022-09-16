import cv2
import numpy as np
cam = cv2.VideoCapture(0)
Image =cv2.imread("tinypic.png",cv2.IMREAD_GRAYSCALE)
output =np.zeros((Image.shape[0],Image.shape[1],3),dtype=Image.dtype)

def RGB_CONV(Image):
    for row in range(Image.shape[0]):
        for value in range(Image.shape[1]):
            if (row%2)==0:
                if (value%2)==0:
                    output[row,value,2] = Image[row,value]
                else:
                    output[row,value,1] = Image[row,value]
            else:
                if (value%2)==0:
                    output[row,value,1] = Image[row,value]
                else:
                    output[row,value,0] = Image[row,value]


def Show_Case(Image,output,cam):
    cv2.imshow("Input",Image)
    cv2.imshow("Output",output)
    while(True):
        ret, pix = cam.read(cv2.COLOR_BGR2HSV)
        hsv = cv2.cvtColor(pix, cv2.COLOR_BGR2HSV)
        lower = np.array([0, 0, 0], np.uint8)
        upper = np.array([200, 255, 100], np.uint8)
        mask = cv2.inRange(hsv, lower, upper)
        cv2.imshow("CAM_COLOR", hsv)
        cv2.imshow("CAM_GRAY", mask)
        k = cv2.waitKey(5) & 0xFF
        # Try to print k ...to se the key numbers
        if k != 255:
            #pass
            cv2.destroyAllWindows()
            break

RGB_CONV(Image)
Show_Case(Image,output,cam)