import cv2 as cv
import numpy as np

def brak_type(img):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    if 0.4 < cv.inRange(hsv, np.array([23,150,150]) ,np.array([28,255,255])).sum()/2560000:
        return 1
    if 0.4 < cv.inRange(hsv, np.array([100,90,90]) ,np.array([140,255,255])).sum()/2560000:
        return 2
    if 0.2 < cv.inRange(hsv, np.array([35,90,90]) ,np.array([45,255,255])).sum()/2560000:
        return 3
    if 0.2 < cv.inRange(hsv, np.array([35,70,20]) ,np.array([65,255,90])).sum()/2560000:
        return 4
    if 0.2 < cv.inRange(hsv, np.array([0,0,0]) ,np.array([255,120,35])).sum()/2560000:
        return 5
    tal = cv.inRange(hsv, np.array([15,0,0]) ,np.array([30,250,250])).sum()/2560000
    kant = cv.Canny(hsv[:,:,2],60,120).sum()
    if 0.65 < tal and kant > 200000:
        return 6
    return 7

def antal_kroner(img):
    ud = [0,0,0,0,0]
    index = 0;
    max_sum = 0;
    teller = 0
    kroner = cv.imread("./king_domino_dataset/krone_master.png")
    for i in range(4):
        ud[i] = cv.matchTemplate(img,kroner,cv.TM_CCOEFF_NORMED)
        kroner = cv.rotate(kroner,cv.ROTATE_90_CLOCKWISE)
        ud[i] = cv.inRange(ud[i], 0.6, 1)
        if ud[i].sum() > max_sum:
            max_sum = ud[i].sum()
            index = i
    if(max_sum > 0):
        ret , markers = cv.connectedComponents(ud[index])
        return ret-1;
    return 0

def poing(img):
    m_img = np.full((5, 5, 3), (255,255,255), dtype=np.uint8)
    ud = np.full((5, 5, 3), (255,255,120), dtype=np.uint8)
    for i in range(5):
        for j in range(5):
            li_img = img[(i*100):(i*100+100),(j*100):(j*100+100)]
            m_img[i,j,0] = brak_type(li_img)
            m_img[i,j,1] = antal_kroner(li_img)
    print(f"---ping:{berging_poing(m_img)}---")

class cl_poing:
    def __init__(self, img, x, y):
        self.img = img
        self.x = x
        self.y = y
        self.col = self.img[x,y,0]
        self.fel = 0
        self.kor = 0 

    def berging_poing(self):
        if(self.img[self.x,self.y,2] == 0) or (self.col == 0) or (self.img[self.x,self.y,0] != self.col):
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
    return tutal

teller = np.random.randint(0,high=74);
while(1):
    img = cv.imread("king_domino_dataset/cropped_and_perspective_corrected_boards/" + str(teller+1) + ".jpg")
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
