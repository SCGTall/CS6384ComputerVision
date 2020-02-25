import cv2
import numpy as np
import sys

if(len(sys.argv) != 3) :
    print(sys.argv[0], ": takes 2 arguments. Not ", len(sys.argv)-1)
    sys.exit()

name_input = sys.argv[1]
name_output = sys.argv[2]

image_input = cv2.imread(name_input, cv2.IMREAD_UNCHANGED);
if(image_input is None) :
    print(sys.argv[0], ": Failed to read image from: ", name_input)
    sys.exit()
cv2.imshow('original image', image_input);

if(len(image_input.shape) != 3 or image_input.shape[2] != 3) :
    print(sys.argv[0], ": not a standard color image: ", name_input)
    sys.exit()

rows, cols, bands = image_input.shape # bands == 3
image_output = np.zeros([rows, cols, bands], dtype=np.uint8)

# this is slow but we are not concerned with speed here
for i in range(0, rows) :
    for j in range(0, cols) :
        b, g, r = image_input[i, j]
        image_output[i,j] = [b, g, r]

cv2.imshow('output image', image_output);
cv2.imwrite(name_output, image_output);



# wait for key to exit

cv2.waitKey(0)
cv2.destroyAllWindows()
