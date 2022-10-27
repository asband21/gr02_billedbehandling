import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import pdb
def maske_prosent(hsv, neder, øver):
    mask = cv.inRange(hsv, neder, øver)
    #cv.imshow("mask",mask)
    return mask.sum()/2560000


def brak_type(img):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
    # mark
    tal = maske_prosent(hsv, np.array([23,150,150]) ,np.array([28,255,255]))
    if 0.4 < tal:
        #cv.imshow("mark"+str(tal),img)
        #print("vand")
        return 1

    # vand
    tal = maske_prosent(hsv, np.array([100,90,90]) ,np.array([140,255,255]))
    if 0.4 < tal:
        #cv.imshow("vand"+str(tal),img)
        #print("vand")
        return 2

    # eng
    tal = maske_prosent(hsv, np.array([35,90,90]) ,np.array([45,255,255]))
    if 0.2 < tal:
        #cv.imshow("eng"+str(tal),img)
        #print("eng")
        return 3

    # skov
    tal = maske_prosent(hsv, np.array([35,70,20]) ,np.array([65,255,90]))
    if 0.4 < tal:
        #cv.imshow("skov"+str(tal),img)
        #print("skov")
        return 4

    # mine
    tal = maske_prosent(hsv, np.array([0,0,0]) ,np.array([255,120,35]))
    if 0.2 < tal:
        #cv.imshow("mine"+str(tal),img)
        #print("mine")
        return 5

    #sump
    tal = maske_prosent(hsv, np.array([15,0,0]) ,np.array([30,250,250]))
    kant = cv.Canny(hsv[:,:,2],60,120).sum()
    print(tal)
    #cv.imshow(str(kant) + " sump "+str(tal),img)
    if 0.65 < tal and kant > 200000:
        #print(kant.sum())
        print("sump")
        return 6

    return 10

def antal_kroner(img):
    #kroner = [0,0,0,0,0]
    ud = [0,0,0,0,0]
    teller = 0
    cv.imshow("felt",img)
    kroner = cv.imread("./king_domino_dataset/krone_master.png")
    for i in range(4):
        ud[i] = cv.matchTemplate(img,kroner,cv.TM_CCOEFF_NORMED)
        kroner = cv.rotate(kroner,cv.ROTATE_90_CLOCKWISE)
        ud[i] = cv.inRange(ud[i], 0.6, 1)
        if ud[i].sum() > 0:
                print(str(ud[i].sum()))
        cv.imshow(str(i),ud[i])
        #cv.waitKey(0)
        cv.imread
    '''
    for i in range(5):
        kroner[i] = cv.imread("./king_domino_dataset/krone_"+str(i) +".png")
        ud[i] = cv.matchTemplate(img,kroner[i],cv.TM_CCOEFF_NORMED)
        cv.imshow(str(i),ud[i])
        ud[i] = cv.inRange(ud[i], 0.5, 1)
        cv.imshow(str(i)+"_maske",ud[i])
        print(str(ud[i].sum())+" sum:"+str(i))
        cv.imshow("tjel:"+str(i),kroner[i])
        if ud[i].sum() > 0:
            cv.waitKey(0)
    '''
    #res = cv.matchTemplate(img,template,cv.TM_CCOEFF)
    #min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    #top_left = min_loc
    #cv.rectangle(img,top_left, bottom_right, 255, 2)
    #print(3)
    return 3

def poing(img):
    print("poing")
    m_img = np.full((5, 5, 3), (255,255,255), dtype=np.uint8)
    for i in range(5):
        for j in range(5):
            li_img = img[(i*100):(i*100+100),(j*100):(j*100+100)]
            m_img[i,j,0] = brak_type(li_img)
            m_img[i,j,1] = antal_kroner(li_img)
    #g = berging_poing(m_img)
    #print(g)
    print("------------")
    print(f"---ping:{berging_poing(m_img)}")
    m_img = cv.cvtColor(m_img, cv.COLOR_HSV2BGR)
    cv.imshow('lille',m_img)


class cl_poing:
    def __init__(self, img, x, y):
        self.img = img
        self.x = x
        self.y = y
        self.col = self.img[x,y,0]
        self.fel = 0
        self.kor = 0 

    def berging_poing(self):
        if(self.img[self.x,self.y,2] == 0):
            return 0
        if(self.col == 0):
            return 0
        #print(f"x:{self.x} y:{self.y}")
        #print("{self.img[self.x,self.y,0]} != {self.col}:")
        #print(f"{self.img[self.x,self.y,0]} != {self.col}:")
        if(self.img[self.x,self.y,0] != self.col):
            return 0
        tutal = 0
        self.img[self.x,self.y,0] = 0
        self.fel = self.fel + 1
        self.kor = self.kor + self.img[self.x,self.y,1]
        li = [[1,0],[-1,0],[0,-1],[0,1]]
        for i in li:
            if -1 < self.x+i[0] < 5 and -1 < self.y+i[1] < 5:
                tmp_x = self.x
                tmp_y = self.y
                self.x = self.x + i[0] 
                self.y = self.y + i[1] 
                self.berging_poing()
                self.x = tmp_x
                self.y = tmp_y 

        return self.fel*self.kor

def berging_poing(img):
    tutal = 0
    for i in range(5):
        for j in range(5):
            tmp = cl_poing(img,i,j)
            t = tmp.berging_poing()
            tutal = tutal + t
            if(t != 0):
                print(f"fellt:{tmp.fel} kroner:{tmp.kor}")
    return tutal

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

teller = 0;
while(1):

    sti = "king_domino_dataset/cropped_and_perspective_corrected_boards/"
    img = cv.imread(sti + str(teller+1) + ".jpg")
    cv.imshow("brat",img)

    k = cv.waitKey(5) & 0xFF
    if k == 110:
        teller = (teller + 1 ) % 74
    if k == 98:
        teller = (teller - 1 ) % 74
    if k == 27:
        break
    if k == 99:
        poing(img)
cv.destroyAllWindows()

