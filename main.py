import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import face 
from math import radians
from statistics import median
def block_mean(image, by_size = 8, bx_size = 8):
    result = image.copy()
    for y in range(0, image.shape[0], by_size):
        for x in range(0, image.shape[1], bx_size):
            sub = result[y:y+by_size, x:x+bx_size]
            sub[:] = np.mean(sub)
    return result
image = face(True)
plt. subplot(121)
plt.imshow(image )
plt.subplot(122)
dimage = image.copy()
res = block_mean(dimage, 32, 32)
plt.imshow(res)
plt.show()