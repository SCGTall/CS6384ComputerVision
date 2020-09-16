# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys

def packagedWarpPerspective(f, u0, v0, a, b, c, w, h):
    m31 = 0 - a
    m32 = 0 - b
    m33 = f + a * (w/2 + u0) + b * (h/2 + v0)
    m11 = c - w / 2 * a
    m12 = 0 - w / 2 * b
    m13 = w / 2 * m33 - c * (w/2 + u0)
    m21 = 0 - h / 2 * a
    m22 = c - h / 2 * b
    m23 = h / 2 * m33 - c * (h/2 + v0)
    matrix = np.mat([[m11, m12, m13], [m21, m22, m23], [m31, m32, m33]])
    return cv2.warpPerspective(input, matrix, (int(round(w)), int(round(h))))

# read arguments
if(len(sys.argv) != 8) :
    print(sys.argv[0], ": takes 7 arguments. Not ", len(sys.argv)-1)
    print("Expecting arguments: python3 ", sys.argv[0], "image f u0 v0 a b c.")
    print("Example:", sys.argv[0], " Missyou.png 4500 0 0 1.2 0.6 2000")
    sys.exit()

image = sys.argv[1]# image
f = float(sys.argv[2])# distance f
u0 = float(sys.argv[3])# principal point (u0, v0)
v0 = float(sys.argv[4])
a = float(sys.argv[5])# 3D plane Z = aX + bY + c
b = float(sys.argv[6])
c = float(sys.argv[7])

# check the correctness of the input parameters
if (f - 0 < 0.0001):# consider the possible inaccurate caused by float
    print("Distance f cannot be zero or negative in real world.")
    sys.exit()
if (c - 0 < 0.0001):
    print("Plane cannot be placed behind the pinhole in real world.")

# read image
print("Processing...")
input = cv2.imread(image, cv2.IMREAD_COLOR)
if(input is None) :
    print(sys.argv[0], ": Failed to read image from: ", image)
    sys.exit()
#cv2.imshow("input image: " + image, input)

# warpPerspective
rows,cols,_ = input.shape
w = float(cols)
h = float(rows)
output = packagedWarpPerspective(f, u0, v0, a, b, c, w, h)

# Show image
cv2.imshow((sys.argv[0]).replace(".py", " output: "), output)
# Save image
cv2.imwrite("cxl190012_outp_1.png", output)

# wait for key to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
