import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label
from skimage.morphology import binary_erosion, binary_dilation, binary_closing

mask = [[0,1,0],[0,1,0],[0,1,0]]
image = np.load("wires6.npy.txt")
labeled = label(image)
for i in range(1,labeled.max()+1):
    one_wire = np.zeros_like(image)
    one_wire[labeled==i] = 1
    erased = binary_erosion(one_wire,mask)
    erased_labeled = label(erased)
    if erased_labeled.max() in [2,3,4]:
        print("Провод под номером ", i , "разделен на ", erased_labeled.max(), "части")
    elif erased_labeled.max() == 1:
        print("Провод под номером ", i , "не разделен ")
    elif erased_labeled.max() == 0:
        print("Провод под номером ", i , "не является проводом, так как его толщина не 3 пикселя")
    else:
        print("Провод под номером ", i , "разделен на ", erased_labeled.max(), "частей")
plt.imshow(labeled)
plt.show()