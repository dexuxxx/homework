import numpy as np
from skimage.morphology import binary_opening, binary_erosion
from skimage.measure import label
import matplotlib.pyplot as plt


img = np.load("ps.npy.txt")

elem = np.asarray([[1,1,0,0,1,1],
                    [1,1,0,0,1,1],
                    [1,1,1,1,1,1],
                    [1,1,1,1,1,1]
                    ])

sqere = np.asarray([[1,1,1,1,1,1],
                    [1,1,1,1,1,1],
                    [1,1,1,1,1,1],
                    [1,1,1,1,1,1]
                    ])
all_objects = 0
sqeres = binary_opening(img, sqere)
sqere_result = label(sqeres)

count = len(np.unique(sqere_result)) - 1
print("Count of sqeres: ", count)
all_objects += count
objects = img - sqeres

for i in range(0,4): #генерировать ряд чисел в рамках заданного диапазона
    
    result = binary_erosion(objects.copy(), elem)
    result = label(result)
    count = len(np.unique(result)) - 1
    all_objects += count

    print("Count of Figure",i,count)
    elem = np.rot90(elem) #пов массива на 90

print ("Count of all objects", all_objects)
