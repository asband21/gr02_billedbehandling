import numpy
import numpy as np
output= np.zeros((3, 3))
green_array=np.zeros((3,3))
c=0

for row in range(3):
    for colum in range(3):
        green_array = output[row ,colum]
        # print(f"Green array: {green_array} in {[ pixel-value,row2-row]}")
        # if 0 != green_array[row2,pixel]:

        numpy.int(green_array[0, 0])
        print(green_array)
        if green_array != 0:
            c = c + 1
print(f" green{green_array}")
print(F"c:{c}")