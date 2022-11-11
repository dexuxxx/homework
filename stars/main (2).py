import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import binary_erosion
from skimage.measure import label

stars = np.load("stars.npy")

mask = [[0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],]

mask2 = [[1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1],]

erostwo = binary_erosion(stars, mask2)
erostwo = label(erostwo)

eros = binary_erosion(stars, mask)
eros = label(eros)

print(eros.max())
print(erostwo.max())
plt.imshow(stars)
plt.show()