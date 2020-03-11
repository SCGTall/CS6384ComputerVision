# -*- coding: utf-8 -*-
import numpy as np
import os
import sys

def readMatrix(ls, keyword):# read matrix from lines according to keyword
    start = 0
    end = 0
    width = 0
    flag = False
    for i in range(len(ls)):
        # found keyword
        if (flag):
            # end if line is blank
            if (0 == len(ls[i].strip().replace('\n', '').replace('\r', ''))):
                end = i
                break
            # get height and width
            else:
                a = ls[i].strip().replace('\n', ' ').replace('\r', ' ').split()
                #print(a)
                if (width < len(a)):
                    width = len(a)
        # not found keyword
        else:
            if (keyword == ls[i].strip().replace('\n', '').replace('\r', '')):
                flag = True
                start = i + 1
        
    if (not flag): return None# return None if never found keyword
    if (0 == end): end = len(ls)
    
    height = end - start
    #print(start, end, width, height)
    array = np.zeros([height, width])
    for i in range(start, end):
        a = ls[i].strip().replace('\n', ' ').replace('\r', ' ').split()
        for j in range(len(a)):
            array[i - start][j] = float(a[j])
        
    return np.mat(array)

def printMatrix(m, size, anchor = None):# print matrix
    for i in range(size[1]):
        sstr = ""
        for j in range(size[0]):
            if (size[0] - 1 != j):
                sstr = sstr + str(m[i, j]) + "\t"
            else:
                sstr = sstr + str(m[i, j])
        
        print(sstr)

    print("Size: ", size)
    if (None == anchor): return 0
    print("Anchor: ", anchor)
    
# main
# inp: input of matrixes.txt
# doFit: fit to image size or not
# mode: cross correlation or convolution
if (len(sys.argv) != 4):
    print(sys.argv[0], ": takes 3 arguments. Not ", len(sys.argv)-1)
    print("Expecting arguments: inp, doFit(T/F), mode(cross correlation: 0/convolution: 1).")
    print("Example:", sys.argv[0], " matrix.txt")
    sys.exit()

inp = sys.argv[1]
if (not os.path.exists(inp)):
    print("1st argument -- dir: ", sys.argv[1], " not exist.")
    sys.exit()
doFit = True
if ("F" == sys.argv[2]):
    doFit = False
elif ("T" != sys.argv[2]):
    print("2nd argument -- doFit: ", sys.argv[2], " can only be T/F.")
    sys.exit()
modeStr = sys.argv[3]
if (("0" != modeStr) and ("1" != modeStr)):
    print("3rd argument -- mode: ", sys.argv[3], " can only be 0/1.")
    sys.exit()
mode = int(modeStr)

f = open(inp, 'r')
lines = f.readlines()

# read matrix
template = readMatrix(lines, "Template")
templateSize = (int(template.shape[1]), int(template.shape[0]))
templateAnchor = (int((templateSize[0]-1)/2), int((templateSize[1]-1)/2))
print("Template:")
printMatrix(template, templateSize, templateAnchor)
if (1 == mode):#flip
    template = np.flip(template)
    templateAnchor = (int(templateSize[0]-1-templateAnchor[0]), int(templateSize[1]-1-templateAnchor[1]))

image = readMatrix(lines, "Image")
imageSize = (int(image.shape[1]), int(image.shape[0]))
imageAnchor = (int((imageSize[0]-1)/2), int((imageSize[1]-1)/2))
print("Image:")
printMatrix(image, imageSize, imageAnchor)

# cross correlation
if (0 == mode):
    print("[cross correlation]:")
else:
    print("[convolution]:")
xOffset = 0 - templateAnchor[0]
yOffset = 0 - templateAnchor[1]
resultSize = (int(imageSize[0]), int(imageSize[1]))
if (not doFit):
    xOffset = 0
    yOffset = 0
    resultSize = (int(imageSize[0] + templateSize[0] - 1), int(imageSize[1] + templateSize[1] - 1))
result = np.zeros([resultSize[1], resultSize[0]])
resultAnchor = (int((resultSize[0]-1)/2), int((resultSize[1]-1)/2))

for j in range(imageSize[1]):
    for i in range(imageSize[0]):
        for q in range(templateSize[1]):
            for p in range(templateSize[0]):
                x = i + p + xOffset
                if ((x < 0) or (x >= resultSize[0])): continue
                y = j + q + yOffset
                if ((y < 0) or (y >= resultSize[1])): continue
                result[y, x] = result[y, x] + template[q, p] * image[j, i]
            
        
    

print("Result:")
printMatrix(result, resultSize, resultAnchor)

f.close()
os.system("read -n 1 -s -p \"Press any key to continue...\"")
print("\n")
