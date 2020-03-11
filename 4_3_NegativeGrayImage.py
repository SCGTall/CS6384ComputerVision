import cv2
import sys
import numpy as np # arrays

# Description:
# Write a program that creates the negative image for a given image. Your program should do the following: • Read an image.
# • Display the input image.
# • If the image is color, convert it into a gray level image.
# • Display the gray level image.
# • Compute the “negative” of the gray level image.
# • Display the negative image.
# • Write the negative image.
# You may want to write your program by modifying the example program “GrayImages.py”.
# argv[1] == target image file.

if(len(sys.argv) != 3) :
    print(sys.argv[0], "takes 2 arguments. Not ", len(sys.argv)-1)
    sys.exit()

name_input = sys.argv[1]
name_output = sys.argv[2]

image_input = cv2.imread(name_input, cv2.IMREAD_UNCHANGED);
if(image_input is None) :
    print(sys.argv[0], "Failed to read image from ", name_input)
    sys.exit()
cv2.imshow('original image', image_input);# Display the input image

rank = len(image_input.shape)
if(rank == 2) :
    gray_image = image_input
elif(rank == 3) :
    gray_image = cv2.cvtColor(image_input, cv2.COLOR_BGR2GRAY)# If the image is color, convert it into a gray level image.
else :
    print(sys.argv[0], "Can't handle unusual image ", name_input)
    sys.exit()

cv2.imshow('gray image', gray_image);# Display the gray level image.
rows, cols = gray_image.shape
image_negative = np.zeros([rows, cols], dtype=np.uint8)

# Compute the “negative” of the gray level image.
for i in range(0, rows) :
    for j in range(0, cols) :
        image_negative[i,j] = 255 - gray_image[i,j]

cv2.imshow('negative image', image_negative);# Display the negative image.
cv2.imwrite(name_output, image_negative);# Write the negative image.

# wait for key to exit

cv2.waitKey(0)
cv2.destroyAllWindows()
