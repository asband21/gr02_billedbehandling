import numpy as np 
import cv2
input = cv2.imread("picture/6.jpg")
crown = cv2.imread("krone_master.png")
mill  = cv2.imread("molle1.png")
where_crown = np.copy(input)
where_crown_array = np.zeros([5, 5])
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
                if ret > 0:
                    where_crown_array[i, j] = ret
    return where_crown_array
#match(input, 0,mill) #only for debuging

# Both have to be turned on #
crop(input,crown)
crop(input,mill)
print(where_crown_array)
cv2.imshow("input",input)
cv2.waitKey(0)

#cv2.imshow("input", input)
#cv2.imshow("template",template)
#cv2.imshow("input_gray", input_gray)
#cv2.imshow("Crop", crop)
#cv2.imshow("Crowns", where_crown)
#cv2.waitKey(0)
cv2.destroyAllWindows()



