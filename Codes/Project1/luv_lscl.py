# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys
from myModules import linear_stretching
from myModules import check_range

# read arguments
if(len(sys.argv) != 7) :
    print(sys.argv[0], ": takes 6 arguments. Not ", len(sys.argv)-1)
    print("Expecting arguments: w1 h1 w2 h2 ImageIn ImageOut.")
    print("Example:", sys.argv[0], " 0.2 0.1 0.8 0.5 fruits.jpg out.png")
    sys.exit()

w1 = float(sys.argv[1])
h1 = float(sys.argv[2])
w2 = float(sys.argv[3])
h2 = float(sys.argv[4])
name_input = sys.argv[5]
name_output = sys.argv[6]

# check the correctness of the input parameters
if(w1<0 or h1<0 or w2<=w1 or h2<=h1 or w2>1 or h2>1) :
    print(" arguments must satisfy 0 <= w1 < w2 <= 1, 0 <= h1 < h2 <= 1")
    sys.exit()

# read image
print("Processing... Please wait until the image appears, then press any key to exit.")
inputImage = cv2.imread(name_input, cv2.IMREAD_COLOR)
if(inputImage is None) :
    print(sys.argv[0], ": Failed to read image from: ", name_input)
    sys.exit()
#cv2.imshow("input image: " + name_input, inputImage)

# check for color image and change w1, w2, h1, h2 to pixel locations
rows, cols, bands = inputImage.shape
if(bands != 3) :
    print("Input image is not a standard color image:", inputImage)
    sys.exit()

W1 = round(w1*(cols-1))
H1 = round(h1*(rows-1))
W2 = round(w2*(cols-1))
H2 = round(h2*(rows-1))

# Cut out target region
image1 = inputImage[H1:H2+1, W1:W2+1, :]
# Change color space
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2Luv)
# Illumination stretching
image3 = np.copy(image2)
image3[:, :, 0] = linear_stretching(image2[:, :, 0])# L
# Convert back to BGR
check_range(image3)# check range
image4 = cv2.cvtColor(image3, cv2.COLOR_Luv2BGR)
check_range(image4)# check range
# Copy back to outputImage
outputImage = np.copy(inputImage)
for i in range(H1, H2+1):
    for j in range(W1, W2+1):
        outputImage[i, j] = image4[i - H1, j - W1]


# Show image
cv2.imshow((sys.argv[0]).replace(".py", ""), outputImage)
# Save image
cv2.imwrite(name_output, outputImage)

# wait for key to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
