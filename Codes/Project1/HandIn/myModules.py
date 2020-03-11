# -*- coding: utf-8 -*-
import cv2
import numpy as np
from collections import Counter
from copy import deepcopy

def linear_stretching(src):
    rows, cols = src.shape
    max = src.max()
    min = src.min()
    tmp = np.copy(src)
    for i in range(rows):
        for j in range(cols):
            tmp[i, j] = round((src[i, j] - min) * 1.0 / (max - min) * 255)


    return tmp

def class_histogram_equalization(src):
    rows, cols = src.shape
    max = src.max()
    min = src.min()
    tmp = np.resize(src, (1, rows * cols))
    h = Counter(tmp[0])
    dict = {}
    last = 0
    for i in range(min, max + 1):
        if (0 == h[i]): continue
        dict[i] = round((last + h[i] / 2.0) * 256 / (rows * cols))
        last = last + h[i]

    tmp = np.copy(src)
    for i in range(rows):
        for j in range(cols):
            tmp[i, j] = dict[src[i, j]]


    return tmp

def check_range(src):
    cl, cu = rec_check(src)
    if ((0 == cl) and (0 == cu)):
        print("No out-of-range behavior.")
    else:
        print("Fix ", cl, " element(s) less than 0, and ", cu, " element(s) more upper 255.")

def rec_check(src):
    cl = 0
    cu = 0
    l = len(src)
    for i in range(len(src)):
        s = src[i]
        if () != src[i].shape:# list
            ecl, ecu = rec_check(src[i])
            cl = cl + ecl
            cu = cu + ecu
        else:# value
            if (src[i] < 0):
                src[i] = 0
                cl = cl + 1
            if (src[i] > 255):
                src[i] = 255
                cu = cu + 1
    return cl, cu