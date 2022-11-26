from collections import deque
import numpy as np
import cv2
input = cv2.imread("4.jpg")
crown = cv2.imread("krone_master.png")
mill = cv2.imread("molle1.png")
where_crown = np.copy(input)
where_crown_array = np.zeros([5, 5])
#what_crown_land = [["blank","blank","blank","blank","blank"],["blank","blank","blank","blank","blank"],["blank","blank","blank","blank","blank"],["blank","blank","blank","blank","blank"],["blank","blank","blank","blank","blank"]]
what_crown_land = np.zeros([5,5])

def average(img, lower, upper,i):
    name = ("water", "farm", "grass", "forest", "cave", "swamp")
    threshold = cv2.inRange(img, lower, upper)
    ##cv.imshow("threshold", threshold)
    # cv2.imshow("threshold " + name[i], threshold) #debuging
    return threshold.sum()/2560000
    ##return threshold.sum()/64000000

def environment(image):
    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)

#water = (h=[140, 160], S[200,255],v)
    avg = average(hsvImage, np.array([140, 220, 0]), np.array([160, 255, 255]), 0)
    #avg = average(hsvImage, np.array([140, 220, 0]), np.array([160, 255, 255]));
    #print("water ="+str(avg))
    if 0.3 < avg:
        return 1

#farm = (h=[30,40], s[220,255], v[170,210])
    avg = average(hsvImage, np.array([30, 220, 160 ]), np.array([40, 255, 210]),1)
    #avg = average(hsvImage, np.array([30, 220, 160]), np.array([40, 255, 210]));
    #print(avg)
    #print("farm ="+str(avg))
    if 0.35 < avg:
        return 2

#grass = (h=[55,75], s[190,255], v[150,215])
    avg = average(hsvImage, np.array([40, 190, 100]), np.array([75, 255, 215]),2)
    #avg = average(hsvImage, np.array([40, 190, 100]), np.array([75, 255, 215]));
    #print(avg)
    #print("grass ="+str(avg))
    if 0.15 < avg:
        return 3

#forest = (h=[62,90], s[118,255], v[37,80])
    avg = average(hsvImage, np.array([62, 90,37]), np.array([90, 255, 80]),3)
    #avg = average(hsvImage, np.array([62, 90, 37]), np.array([90, 255, 80]));
    #print(avg)
    #print("forest ="+str(avg))
    if 0.10 < avg:
        return 4

#cave = (h[10,25], s[0,55], v[30,75])
    avg = average(hsvImage, np.array([150, 0, 0]), np.array([255, 124, 78]),4)
    #avg = average(hsvImage, np.array([0, 0, 0]), np.array([52, 124, 78]));
    #print(avg)
    #print("cave ="+str(avg))
    if 0.10 < avg:
        return 5

#swamp = (h[14,39], s[90,189], v[70,165])
    avg = average(hsvImage, np.array([14, 0, 70]), np.array([39, 189, 165]),5)
    #avg = average(hsvImage, np.array([14, 90, 70]), np.array([39, 189, 165]));
    #print(avg)
    #print("swamp ="+str(avg))
    if 0.30 < avg:
        return 6

    print("..........") # only for debugging in the terminel

def match (img_crop,t,template):
    rotaion_array = [0, 0, 0, 0]
    for i in range(4):
        rotaion_array[i] = cv2.matchTemplate(img_crop, template, cv2.TM_CCOEFF_NORMED)  #gets match
        template = cv2.rotate(template, cv2.ROTATE_90_CLOCKWISE)# rotaions the template
        rotaion_array[i] = cv2.inRange(rotaion_array[i], 0.62, 1)# theresdhold of the matchtemplate
        #cv2.imshow("rotation:"+str(i), rotaion_array[i])
        # cv2.waitKey(0)
        #cv2.imshow("rotation" + str(i) + "_" + str(t), rotaion_array[i])
        #where_crown = cv2.connectedComponents(rotaion_array[i])


    # want to see how the matches works, use this
    #rotaion_array1= cv2.matchTemplate(input, template, cv2.TM_CCOEFF_NORMED)
    #rotaion_array1 = cv2.inRange(rotaion_array1, 0.62, 1) #This makes the template binary if within thereshold
    #cv2.imshow("rotation:" , rotaion_array1)
    return rotaion_array

def crop (image,temp_crown):
    img = image.copy()
    for i in range(5):
        for j in range(5):
            crop = img[i*100:i*100+100, j*100:j*100+100]
            for g in match(crop, i+j,temp_crown):
                ret, marks = cv2.connectedComponents(g)
                ret = ret-1
                what_crown_land[i][j] = environment(crop)

                if ret > 0:
                    #cv2.imshow("crop", crop)
                    #cv2.waitKey(0)
                    where_crown_array[i, j] = ret


    return where_crown_array


def ignite_pixel(image, coordinate, id):
    y, x = coordinate
    burn_queue = deque()
    tiles = what_crown_land
    if image[y, x] > 0 and tiles[y,x] < 10:
        burn_queue.append((y, x))
    '''tiles = environment(size)
    img = image[y,x]
    print(image[y,x])
    print(tiles)
    if img == tiles:
        print("nice")'''
    while len(burn_queue) > 0:
        current_coordinate = burn_queue.pop()
        y, x = current_coordinate
        print(len(burn_queue))
        if x + 1 < image.shape[1] and tiles[y, x + 1] == tiles[y, x]:
            burn_queue.append((y, x + 1))
            #print("højre")

        if y + 1 < image.shape[0] and tiles[y + 1, x] == tiles[y, x]:
            burn_queue.append((y + 1, x))
            #print("ned")

        if x - 1 >= 0 and tiles[y, x - 1] == tiles[y, x]:
            burn_queue.append((y, x - 1))
            #print("venstre")

        if y - 1 >= 0 and tiles[y - 1, x] == tiles[y, x]:
            burn_queue.append((y - 1, x))
            #print("op")
        tiles[y, x] = id

        #print(image)
        #print(burn_queue)
        #input()

        if len(burn_queue) == 0:
            return id + 10
            # print(len(burn_queue))
        print(current_coordinate)
        #print("......................")
    #print(tiles)
    return id


def grassfire(array):
    next_id = 10
    for y, row in enumerate(array):
        for x, pixel in enumerate(row):
            next_id = ignite_pixel(array, (y, x), next_id)
            print(next_id)
            print("1")



#match(input, 0,mill) #only for debuging

# Both have to be turned on #

crop(input, crown)
crop(input, mill)
print(what_crown_land)
print(where_crown_array)
#print(what_crown_land)
#print(where_crown_array)

grassfire(where_crown_array)





cv2.imshow("input",input)
cv2.waitKey(0)
#cv2.imshow("input", input)
#cv2.imshow("template",template)
#cv2.imshow("input_gray", input_gray)
#cv2.imshow("Crop", crop)
#cv2.imshow("Crowns", where_crown)
#cv2.waitKey(0)
cv2.destroyAllWindows()



