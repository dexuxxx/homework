import numpy as np
import matplotlib.pyplot as plt
from os import listdir
import skimage
from skimage import filters
from skimage.measure import label,regionprops
from skimage.filters import  gaussian
from skimage.color.colorconv import rgb2gray
from skimage.filters import threshold_otsu

path = 'images/'
files = [file for file in listdir(path)]
pencils_sum = 0

def proces(img):
    img = np.mean(img,2)
    img = gaussian(img, sigma=19)
    threshold = filters.threshold_otsu(img)
    img[img < threshold] = 0
    img[img > 0] = 1
    img = skimage.util.invert(img)
    labeled = label(img)
    return labeled

for file in files:

    img = plt.imread(path + file)


    labeled = proces(img)
    regions = regionprops(labeled)
    sum = 0
   
    for region in regions:
        cur_area = region.equivalent_diameter
        centr = region.eccentricity

        if centr > 0.99 and cur_area > 500:
            sum += 1

    pencils_sum += sum

    print("Image ", path + file," - ", sum, " pencils")
    
    plt.subplot(121)
    plt.imshow(img)
    plt.subplot(122)
    plt.imshow(labeled)
    plt.show()

print("Number of pencils: ", pencils_sum)