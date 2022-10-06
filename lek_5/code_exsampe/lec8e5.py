import numpy as np


def dilation(img, x, y, k_size):
    mid = int(k_size / 2)
    for x_step in range(k_size):
        x_c = x + (x_step - mid)
        if x_c < 0 or x_c >= len(img):  # if current x is outside the image
            continue
        for y_step in range(k_size):
            y_c = y + (y_step - mid)
            if y_c < 0 or y_c >= len(img[x_c]):  # if current y is outside the image
                continue
            if img[y_c, x_c] == 1:  # if any part of our kernel hits
                return 1
    return 0


def erosion(img, x, y, k_size):
    if img[y, x] == 0:
        return 0
    mid = int(k_size / 2)
    fit = True
    for x_step in range(k_size):
        x_c = x + (x_step - mid)
        if x_c < 0 or x_c >= len(img):  # if current x is outside the image
            continue
        for y_step in range(k_size):
            y_c = y + (y_step - mid)
            if y_c < 0 or y_c >= len(img[x_c]):  # if current y is outside the image
                continue
            if img[y_c, x_c] != 1:  # if any part of our kernel does not hit
                fit = False
    if fit:
        return 1
    else:
        return 0


if __name__ == '__main__':
    test = np.asarray([[1, 0, 0, 1, 1, 1, 0, 0],
                       [1, 0, 0, 1, 1, 1, 0, 0],
                       [1, 0, 0, 1, 1, 1, 1, 0],
                       [0, 0, 0, 0, 1, 1, 1, 0],
                       [0, 0, 0, 0, 0, 1, 1, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0],
                       [1, 0, 0, 0, 0, 0, 1, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0]])
    for row in test:
        print(row)
    dilated = np.zeros(test.shape, dtype=np.uint8)
    eroded = np.zeros(test.shape, dtype=np.uint8)
    for x, row in enumerate(test):
        for y, pixel in enumerate(row):
            dilated[y, x] = dilation(test, x, y, 3)
            eroded[y, x] = erosion(test, x, y, 3)
    print()
    for row in dilated:
        print(row)
    print()
    for row in eroded:
        print(row)
