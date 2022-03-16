import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys
import struct
import os
from itertools import groupby

np.set_printoptions(threshold=sys.maxsize)


def rle(channel):
    count = 1
    temp = ""
    list = []  # (value,numbers)
    for i in range(0, len(channel), 2):
        for j in range(int(channel[i + 1])):
            list.append(channel[i])
    return list


if __name__ == '__main__':

    img = []
    with open('img1_compress.2036', 'r') as f:
        for line in f:
            item = line[:-1]
            img.append(item)

    list_blue = []
    list_green = []
    list_red = []

    list_blue = img[5:int(img[2]) + 5]
    list_green = img[5 + int(img[2]):5 + int(img[2]) + int(img[3])]
    list_red = img[5 + int(img[2]) + int(img[3]):5 + int(img[2]) + int(img[3]) + int(img[4])]

    blue = rle(list_blue)
    green = rle(list_green)
    red = rle(list_red)

    array_blue = np.array(blue, np.uint8)
    array_green = np.array(green, np.uint8)
    array_red = np.array(red, np.uint8)

    array_blue = array_blue.reshape(int(img[0]), int(img[1]), 1)
    array_green = array_green.reshape(int(img[0]), int(img[1]), 1)
    array_red = array_red.reshape(int(img[0]), int(img[1]), 1)

    rgb_img = cv2.merge([array_blue, array_green, array_red])

    print(rgb_img.shape)
    cv2.imwrite("img1_decode.bmp", rgb_img)




