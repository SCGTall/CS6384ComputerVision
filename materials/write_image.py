import cv2
import numpy as np # write numpy arrays as images


# Create a matrix
X = np.matrix('1 2; 3 4') # 2x2 matrix. semicolon separates rows
print("X=", X)

y = np.matrix('1;2'); print("y=", y) # 2x1 matrix


# Matrix can also be created from a 1D array by reshaping it
w = np.array([1,2,3,4,5,6]); print("w=", w)
W = w.reshape(3, 2); print("W=", W)

# Equivalently:
W = np.array([1,2,3,4,5,6]).reshape(3, 2); print("W=", W)

# color img stores as 3-d tensor [height, width, BGR]
color1 = np.zeros((30, 100, 3), dtype='uint8')
color1[:10, :, 0] = 255  # first 10 rows are set to blue
color1[10:20, :, 1] = 255 
color1[20:30, :, 2] = 255 

cv2.namedWindow('write_window', cv2.WINDOW_AUTOSIZE)
cv2.imshow('write_window', color1)
cv2.imwrite('RGB_eg.jpg', color1) # don't write image as jpg
cv2.imwrite('RGB_eg.png', color1)

# wait for key to exit

cv2.waitKey(0)
cv2.destroyAllWindows()
