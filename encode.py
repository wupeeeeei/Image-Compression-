import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys
import struct
import os
import pickle

np.set_printoptions(threshold=sys.maxsize)


def rle(channel):
    count = 1
    temp = 0
    list = []  # (value,numbers)
    for i in range(len(channel) - 1):
        temp = channel[i]
        if channel[i + 1] == channel[i]:
            if i + 1 == len(channel) - 1:
                list.append(temp)
                list.append(count)
            else:
                count += 1
            continue
        else:
            list.append(temp)
            list.append(count)
            count = 1
    # last char
    if channel[len(channel) - 1] == channel[len(channel) - 2]:
        # print(len(list))
        a = int(list[len(list) - 1])
        list[len(list) - 1] = a + 1
    else:
        # print(len(list))
        list.append(channel[len(channel) - 1])
        list.append(1)
    return list


if __name__ == '__main__':

    img = cv2.imread("img1.bmp")
    # print(img.shape)
    blue, green, red = cv2.split(img)  # r,g,b切割

    blue = blue.flatten()
    green = green.flatten()
    red = red.flatten()

    blue = blue.tolist()
    green = green.tolist()
    red = red.tolist()

    list_blue = rle(blue)
    list_green = rle(green)
    list_red = rle(red)

    list = [img.shape[0], img.shape[1], len(list_blue), len(list_green), len(list_red)]
    list = list + list_blue + list_green + list_red
    # print(len(list_blue),len(list_green),len(list_red))

    print(list[2], list[3], list[4])

    with open("img1_compress.2036", "w") as f:
        for item in list:
            f.write('%s\n' % item)
    f.close()

