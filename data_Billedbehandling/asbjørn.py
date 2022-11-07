import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import pdb
def afstan(p1, p2, dim):
    d = 0
    for i in range(dim):
        d = d + (p2[i]-p1[i])**2
    return math.sqrt(d)

def er_min(tal, li):
    over = [0,0]
    for i in len(li):
        if tal < li[i]
            



def knn(list_data, pungt, naboer, dim):
    li = []
    for i in range(naboer):
        li.append([afstan(list_data[0,i],pungt)),0])

    for i in range(len(list_data)):
        for j in list_data[i]:



data1 = np.loadtxt("./trainClass1.dat")
data2 = np.loadtxt("./trainClass2.dat")
data3 = np.loadtxt("./trainClass3.dat")
data4 = np.loadtxt("./trainClass4.dat")
datau = np.loadtxt("./unknown.dat")

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.scatter(data1[:,1],data1[:,2],data1[:,3],color = "green")
ax.scatter(data2[:,1],data2[:,2],data2[:,3],color = "red")
ax.scatter(data3[:,1],data3[:,2],data3[:,3],color = "blue")
ax.scatter(data4[:,1],data4[:,2],data4[:,3],color = "black")
ax.scatter(datau[:,1],datau[:,2],datau[:,3],color = "yellow")
#plt.stackplot(data[:,1],data[:,2])
plt.show()
