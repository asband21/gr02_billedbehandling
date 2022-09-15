import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import pdb


def sum_xy(array, start, stop, x_len, y_len):
    tal = [0,0,0]
    for x in range(start,x_len+start):
        for y in range(stop,y_len+stop):
            tal[0] = tal[0] + array[x,y][0]
            tal[1] = tal[1] + array[x,y][1]
            tal[2] = tal[2] + array[x,y][2]
    for i in range(3):
        tal[i] = tal[i]/(x_len*y_len)
    return tal


#pdb.set_trace()
#cap = cv.VideoCapture(0)
teller = 0;
while(1):
#for teller in range(74):
#    _, frame = cap.read()
#    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    sti = "king_domino_dataset/cropped_and_perspective_corrected_boards/"
    img = cv.imread(sti + str(teller+1) + ".jpg")
    print(sti + str(teller+1) + ".jpg")
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    m_img = np.full((5, 5, 3), (0,0,0), dtype=np.uint8)
    
    for i in range(0):
        for j in range(5):
            #pdb.set_trace()
            mid = sum_xy(img,i*100,j*100,100,100)
            m_img[i,j,0] = int(mid[0])
            m_img[i,j,1] = int(mid[1])
            m_img[i,j,2] = int(mid[2])
            #print(str(m_img[i,j,0])+"\t"+ str(m_img[i,j,1])+"\t" + str(m_img[i,j,2]))
    sm_img =  cv.cvtColor(m_img, cv.COLOR_BGR2HSV)
    #plt.clf()
    #plt.scatter(sm_img[:,:,0], sm_img[:,:,2])
    #plt.draw()
    #plt.pause(0.001)
    
    #vand
    lower_vand = np.array([100,90,90])
    upper_vnad = np.array([140,255,255])
    mask = cv.inRange(hsv, lower_vand, upper_vnad)
    res_vand = cv.bitwise_and(img,img, mask= mask)
    cv.imshow('vand',res_vand)
    
    #eng
    lower_eng = np.array([39,90,90])
    upper_eng = np.array([45,255,255])
    mask = cv.inRange(hsv, lower_eng, upper_eng)
    res_eng = cv.bitwise_and(img,img, mask= mask)
    cv.imshow('eng',res_eng)
    
    #sump
    lower_sump = np.array([15,0,0])
    upper_sump = np.array([30,200,200])
    mask = cv.inRange(hsv, lower_sump, upper_sump)
    res_sump = cv.bitwise_and(img,img, mask= mask)
    cv.imshow('sump',res_sump)
    
    #mark
    lower_mark = np.array([23,150,150])
    upper_mark = np.array([28,255,255])
    mask = cv.inRange(hsv, lower_mark, upper_mark)
    res_mark = cv.bitwise_and(img,img, mask= mask)
    cv.imshow('mark',res_mark)

    #skov
    lower_skov = np.array([35,70,20])
    upper_skov = np.array([65,255,90])
    mask = cv.inRange(hsv, lower_skov, upper_skov)
    res_skov = cv.bitwise_and(img,img, mask= mask)
    cv.imshow('skov',res_skov)
    
    #mine
    lower_mine = np.array([0,0,0])
    upper_mine = np.array([255,120,35])
    mask_mine = cv.inRange(hsv, lower_mine, upper_mine)
    res_mine = cv.bitwise_and(img,img, mask= mask)
    cv.imshow('mine',mask_mine)
    
    #"""
    #kant
    kant = cv.Canny(hsv[:,:,2],60,120)
    cv.imshow('kant',kant)
    
    #går kant
    grå = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    kant = cv.Canny(grå,104,105)
    cv.imshow('gor kant',hsv[:,:,1])

    #sobel
    sobel_x = cv.Canny(img,10,50)
    sobel_y = cv.Canny(img,10,200)
    sob_img = cv.Sobel(cv.cvtColor(img, cv.COLOR_BGR2GRAY), cv.CV_16S , 2 ,2, ksize=9, scale=10, delta=0, borderType=cv.BORDER_DEFAULT)
    #sob_img = cv.inRange(sob_img,150,255)
    cv.imshow('sobel',sob_img)
    #"""
    cv.imshow('brat',img)
    cv.imshow('lille',m_img)
    #cv.imshow('lille_2',sm_img)
    #cv.imshow('mask',mask)
    #pdb.set_trace()
    #print('Image Width is',img.shape[1])
    #print('Image Height is',img.shape[0])
    #print(" ")
    k = cv.waitKey(5) & 0xFF
    #print(sti + str(teller+1) + ".jpg    " , end="\r")
    if k == 110:
        teller = (teller + 1 ) % 74
    if k == 98:
        teller = (teller - 1 ) % 74
    if k == 99:
        print("lower hsv bound")
    if k == 27:
        break
cv.destroyAllWindows()
print("                                                                                                  ")
