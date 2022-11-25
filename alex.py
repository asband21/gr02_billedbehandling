#get the image
import cv2
import numpy as np
import math
board = cv2.imread("lek_4_neighborhood_processing/20.jpg")		#det udvalgte board indsættes
R = 0
cv2.imshow("window",board)
B = 0
G = 0									#her er R,G,B sat til 0, disse bliver brugt til beregne den totale rød,grøn,blå værdi senere
gf = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
									#devide the image into the tiles
for l in range(0,500,100): 
	for h in range (0,500,100):					#boardet opskæres i tiles som er 100 x 100 pixels
		tiles =board[l:l+100,h:h+100] 				#det enkelte tile bliver deffineret	
	#	print(f"l{l} h{h}")
	#	l= l
	#	h= h
#		cv2.imshow("tile:"+str(l)+"_"+str(h),tiles)
		cv2.imshow(str(int(l/100))+str(int(h/100)),tiles)	#de enkelte tiles vises 
		for x in range(tiles.shape[0]):
			for y in range(tiles.shape[1]):
				r = (tiles[x,y,0])
				b = (tiles[x,y,1]) 
				g = (tiles[x,y,2])
				sumofr = np.sum(tiles[x,y,[0]])
				R = R+r
				B = B+b 
				G = G+g					#rgb tages ud af hvert tile enkeltvis og rgb bliver lagt sammen for hvert tile
	#printing r value					
#		print(R)
		ø=R/500
		print(f"ø:{ø}")
#		R=0

# printing b value                                       
#		print(B)
		o=B/500
		print(f"o:{o}")
#		B=0
#print g
#		print(G)
		a=G/500
#		G=0
		print(f"a:{a}")
		print("new tile")				#de enkelt værdier divideres med 500 for at gøre værdierne mere overskuelige samt få dem til at passe ind i de senere angivne t										theshholds
#		hsv = np.array [ø,o,a]     
		R=0
		B=0
		G=0
								#RGB resættes					

		if (2300<ø<3680 and 1727<o<2061 and 84<a<1147):
			print ("water") 
			print(f"l:{l} h:{h}")		
			gf[int(l/100),int(h/100)] = 1
		elif (1500<ø<1580 and 2873<o<2893 and 2900<a<2950):
			print ("midt")
			print(f"l:{l} h:{h}")		
			gf[int(l/100),int(h/100)] = 2
		elif (302<ø<560 and 1335<o<1368 and 990<a<1123):
			print ("tree")
			print(f"l:{l} h:{h}")		
			gf[int(l/100),int(h/100)] = 3
		elif (148<ø<555 and 3054<o<3487 and 3582<a<3989):
			print ("wheatfield")
			print(f"l:{l} h:{h}")		
			gf[int(l/100),int(h/100)] = 4
		elif (700<ø<746 and 1150<o<2893 and 1300<a<1586):
			print ("mine")
			print(f"l:{l} h:{h}")		
			gf[int(l/100),int(h/100)] = 5
		elif (581<ø<769 and 2544<o<3202 and 2070<a<2413):
			print("grass")
			print(f"l:{l} h:{h}")		
			gf[int(l/100),int(h/100)] = 6
		elif (1080<ø<1358 and 2019<o<3202 and 2281<a<2636):
			print("midlands")
			print(f"l:{l} h:{h}")		
			gf[int(l/100),int(h/100)] = 7
		else:
			print ("skyd mig")
			print(f"l:{l} h:{h}")		
			gf[int(l/100),int(h/100)] = 8		#threshholds angives
			

print (gf) 							#der bliver printet et grid af grassfire arrayet
i = 1
def grassfire(x,y,gf,i):

	if i == gf[x,y]:
		count = 1
		gf[x,y] = 0
		if y != 4:
			if gf[x,y+1] == i:
				count = count + grassfire(x,y+1,gf,i)
		if x != 4:
			if gf[x+1,y] == i:	
				count = count + grassfire(x+1,y,gf,i)
		if x != 0:	
			if gf[x-1,y] == i:
				count = count + grassfire(x-1,y,gf,i)
		if y != 0 : 	
			if gf[x,y-1] == i:	
				count = count + grassfire(x,y-1,gf,i)
		return count
	return 0
								#grassfire funktion


v = 0 								# v deffineres, bliver senere brugt til at se om alle tiles er fundet
print("i:")
for i in range (1,8,1):
	for x in range (5):
		for y in range (5):				#der bliver søgt efter hvert type tile
			
			#:grassfire(x,y,gf,i)	
			k = grassfire(x,y,gf,i)
			if k != 0:
				print(k)
				v = v+k
print(v)	
								#de enkelte værdier for hvert klump og totalværdien printes


	
#find the color of the tile
#print("tile color")
#print(board)
#find the starting square
#how to find a crown
#find out where the squares with the crowns are
#see if there is anything that differentiates the different squares 
#note if the squares have any similar square sides touching another?

#cv2.imshow("tile1",tiles) 
cv2.waitKey(0)
