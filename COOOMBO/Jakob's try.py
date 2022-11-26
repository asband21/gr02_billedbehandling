from collections import deque
import numpy as np
import cv2
input = cv2.imread('picture/3.jpg')
crown = cv2.imread('krone_master.png')
mill = cv2.imread('molle1.png')
where_crown_array = np.zeros([5, 5])
what_crown_land = np.zeros([5,5])

def average(img, lower, upper):
    threshold = cv2.inRange(img, lower, upper)
    return threshold.sum()/2560000


def environment(image):
    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)

#water
    avg = average(hsvImage, np.array([140, 220, 0]), np.array([160, 255, 255]))

    if 0.3 < avg:
        return 1

#farm
    avg = average(hsvImage, np.array([30, 220, 160 ]), np.array([40, 255, 210]))

    if 0.35 < avg:
        return 2

#grass
    avg = average(hsvImage, np.array([40, 190, 100]), np.array([75, 255, 215]))

    if 0.15 < avg:
        return 3

#forest
    avg = average(hsvImage, np.array([62, 90,37]), np.array([90, 255, 80]))
    if 0.10 < avg:
        return 4

#cave
    avg = average(hsvImage, np.array([150, 0, 0]), np.array([255, 124, 78]))
    if 0.10 < avg:
        return 5

#swamp
    avg = average(hsvImage, np.array([14, 0, 70]), np.array([39, 189, 165]))
    if 0.30 < avg:
        return 6


def match (img_crop,template):
    rotaion_array = [0, 0, 0, 0]
    for i in range(4):
        rotaion_array[i] = cv2.matchTemplate(img_crop, template, cv2.TM_CCOEFF_NORMED)  #gets match
        template = cv2.rotate(template, cv2.ROTATE_90_CLOCKWISE)# rotaions the template
        rotaion_array[i] = cv2.inRange(rotaion_array[i], 0.62, 1)# theresdhold of the matchtemplate
    return rotaion_array

def crop (image,temp_crown):
    img = image.copy()
    for i in range(5):
        for j in range(5):
            crop = img[i*100:i*100+100, j*100:j*100+100]
            for g in match(crop,temp_crown):
                obj, cod = cv2.connectedComponents(g)
                obj = obj-1
                what_crown_land[i,j] = environment(crop)
                if obj > 0:
                    where_crown_array[i, j] = obj
    return where_crown_array


def ignite_pixel(image, coordinate, id):
    y, x = coordinate
    burn_queue = deque()
    crown_count = 0
    count_land_types = 0

    if image[y, x] < 10:
        burn_queue.append((y, x))

    while len(burn_queue) > 0:
        current_coordinate = burn_queue.pop()
        y, x = current_coordinate

        if image[y, x] < 10:
            if x + 1 < image.shape[1] and image[y, x + 1] == image[y, x]:
                burn_queue.append((y, x + 1))
            if y + 1 < image.shape[0] and image[y + 1, x] == image[y, x]:
                burn_queue.append((y + 1, x))
            if x - 1 >= 0 and image[y, x - 1] == image[y, x]:
                burn_queue.append((y, x - 1))
            if y - 1 >= 0 and image[y - 1, x] == image[y, x]:
                burn_queue.append((y - 1, x))
        count_land_types += 1
        crown_count = where_crown_array[y, x] + crown_count
        image[y, x] = id
        if len(burn_queue) == 0:
            if crown_count*count_land_types > 0:
                print(f" there is {count_land_types} tail of this type and {crown_count} crowns which is a total of {crown_count * count_land_types} points")
                print("........")
            return id + 10
    return id


def grassfire(image):
    next_id = 10
    for y, row in enumerate(image):
        for x, pixel in enumerate(row):
            next_id = ignite_pixel(image, (y, x), next_id)


crop(input, crown)
crop(input, mill)
print("Count of crowns")
print(where_crown_array)
print ("Cronw's land")
print(what_crown_land)
grassfire(what_crown_land)
print(what_crown_land)
cv2.imshow("input",input)
cv2.waitKey(0)
cv2.destroyAllWindows()
