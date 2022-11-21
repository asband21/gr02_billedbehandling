#get the image
import cv2
import numpy as np
import math
board = cv2.imread("lek_4_neighborhood_processing/20.jpg")
R = 0
cv2.imshow("window",board)



#devide the image into the tiles
for l in range(0,500,100): 
	for h in range (0,500,100):	
		tiles =board[l:l+100,h:h+100]
	#	print(f"l{l} h{h}")
	#	l= l
	#	h= h
		for L in range(0,500,100):
			for H in range(100,500,100):
#				cv2.imshow("tile:"+str(l)+"_"+str(h),tiles)
				cv2.imshow(str(int(l/100))+str(int(h/100)),tiles)
				for x in range(tiles.shape[0]):
					for y in range(tiles.shape[1]):
						r = (tiles[x,y,[0]])
						b = (tiles[x,y,[1]]) 
						g = (tiles[x,y,[2]])
						sumofr = np.sum(tiles[x,y,[0]])
						R = R+r
		print(sumofr)			
		print(R)


#find the color of the tile
print("tile color")
#print(board)
#find the starting square
#how to find a crown
#find out where the squares with the crowns are
#see if there is anything that differentiates the different squares 
#note if the squares have any similar square sides touching another?

cv2.imshow("tile1",tiles) 
cv2.waitKey(0)

