import numpy as np
import cv2


# Sobel edge detection
def apply_kernel(img, kernel):
    output = np.zeros(img.shape)
    h = len(img)
    w = len(img[0])
    for y, row in enumerate(img):
        for x, pixel in enumerate(row):
            if x > 1 and x + 1 < w and y > 1 and y + 1 < h:
                output[y, x] = np.sum(np.multiply(img[y - 1:y + 2, x - 1:x + 2], kernel))
    return output


def get_magnitude(img):
    output = np.sqrt(img ** 2)
    return output


if __name__ == '__main__':
    sobel_kernel_horizontal = np.asarray([[-1, 0, 1],
                                          [-2, 0, 2],
                                          [-1, 0, 1]])
    sobel_kernel_vertical = np.asarray([[1, 2, 1],
                                        [0, 0, 0],
                                        [-1, -2, -1]])

    # Load image and convert to float32 in order to have negative numbers.
    img = np.asarray(cv2.imread("shapes.png", cv2.IMREAD_GRAYSCALE), dtype=np.float32)

    # img_horizontal = cv2.filter2D(img, -1, sobel_kernel_horizontal) # How to do it with opencv2
    img_horizontal = apply_kernel(img, sobel_kernel_horizontal)
    img_horizontal = get_magnitude(img_horizontal)
    # img_vertical = cv2.filter2D(img, -1, sobel_kernel_vertical)# How to do it with opencv2
    img_vertical = apply_kernel(img, sobel_kernel_vertical)
    img_vertical = get_magnitude(img_vertical)

    sobel_edge_detected = img_horizontal + img_vertical
    # As we now have a float32 image values can go above 255. In cases where both horizontal and vertical detection has
    # positive response the result will be: 510 (sqrt(255)^2 + sqrt(255)^2)
    # Therefore, where image is above 255, set to 255
    sobel_edge_detected[sobel_edge_detected > 255] = 255

    cv2.imshow("shapes", img)
    cv2.imshow("img_horizontal", img_horizontal)
    cv2.imshow("img_vertical", img_vertical)
    cv2.imshow("sobel_edge_detected", sobel_edge_detected)
    cv2.waitKey(0)
