# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import os

plt.figure("image")
# circle
p0x = [3, 1]
p0y = [3, 5]
p0s = [18000, 18000]
plt.scatter(p0x, p0y, s = p0s, c = "green", alpha = 0.5, ) # huge point for circle
# points
px = [1, 2, 2, 3, 3]
py = [3, 1, 5, 3, 5]
plt.scatter(px, py, s = 50, c = "blue")
# axis
plt.axis("equal")
plt.xlim(-3, 8)
plt.ylim(0, 8)
plt.xticks(np.arange(-3, 9, 1))
plt.yticks(np.arange(0, 9, 1))
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.draw()

os.system("read -n 1 -s -p \"Press any key to continue...\"")
print("\n")

plt.savefig("Homework-7Image.png")
plt.close()