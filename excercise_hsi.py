import cv2 as cv
import numpy as np
import pdb
import math as ma

verboos = False

cap = cv.VideoCapture(0)

def bgr2hsi(img):
    size = img.shape
    for i in range(1,size[0]-1):
        for j in range(1,size[1]-1):
            B = 0
            G = 0
            R = 0
            H = 0.000000001
            I = 0.000000001
            S = 0.000000001
            B = B + img[i,j,0]
            G = G + img[i,j,1]
            R = R + img[i,j,2]
            if R+G+B == 0:
                continue
            if R&G&B == 255:
                img[i,j] = [255,255,255]
                continue
            I =  (R+G+B)/3
            S = 1-3*min(R,B,G)/(R+G+B)
            S = S*255
            if verboos:
                print("-------------------")
                print(R)
                print(G)
                print(B)
                print(((R-G)+(R-B))/(2*ma.sqrt((R-G)*(R-G)+(R-B)*(G-B))))
            H = ma.acos(((R-G)+(R-B))/(2*ma.sqrt((R-G)*(R-G)+(R-B)*(G-B))))
            if G < B:
                H = ma.pi*2-H
            H = (H*255)/ma.pi*2-H
            if ma.isnan(H):
                H = 255
            if ma.isnan(S):
                S = 255
            if ma.isnan(I):
                I = 255
            img[i,j,0] = int(H)
            img[i,j,1] = int(S)
            img[i,j,2] = int(I)
    return img

def bgr2hsv(img):
    size = img.shape
    for i in range(1,size[0]-1):
        for j in range(1,size[1]-1):
            B = 0
            G = 0
            R = 0
            H = 0.000000001
            I = 0.000000001
            S = 0.000000001
            B = B + img[i,j,0]
            G = G + img[i,j,1]
            R = R + img[i,j,2]
            if R+G+B == 0:
                continue
            if R&G&B == 255:
                img[i,j] = [255,255,255]
                continue
            v =  max(R,G,B)
            S = (v-min(R,G,B))/v
            S = S*255
            if verboos:
                print("-------------------")
                print(R)
                print(G)
                print(B)
            if R == v and G >= B:
                H = (G-B)*42.66666666/(v-min(R,G,B))
            elif G == v:
                H = ((B-R)/((v-min(R,G,B)))+2)*42.66666666
            elif B == v:
                H = ((R-G)/((v-min(R,G,B)))+4)*42.66666666
            elif v == R and G < B:
                H = ((R-B)/((v-min(R,G,B)))+4)*42.66666666
            else:
                print("-------------------")
                print(R)
                print(G)
                print(B)
                print("fejl prøv iegn")
                exit()
            if ma.isnan(H):
                H = 255
            if ma.isnan(S):
                S = 255
            if ma.isnan(v):
                I = 255
            img[i,j,0] = int(H)
            img[i,j,1] = int(S)
            img[i,j,2] = int(v)
    return img

while(1):
    _, frame = cap.read()
    frame = frame[100:200,100:200,:]
    HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    min_hsi = bgr2hsi(frame.copy())
    min_hsv = bgr2hsv(frame.copy())
    cv.imshow('ind',frame)
    cv.imshow('HSV_H',HSV[:,:,0])
    cv.imshow('HSV_S',HSV[:,:,1])
    cv.imshow('HSV_V',HSV[:,:,2])
    cv.imshow('min_HSI_H',min_hsi[:,:,0])
    cv.imshow('min_HSI_S',min_hsi[:,:,1])
    cv.imshow('min_HSI_I',min_hsi[:,:,2])
    cv.imshow('min_HSV_H',min_hsv[:,:,0])
    cv.imshow('min_HSV_S',min_hsv[:,:,1])
    cv.imshow('min_HSV_I',min_hsv[:,:,2])
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
