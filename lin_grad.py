import matplotlib.pyplot as plt
import numpy as np

def lerp(color1, color2, t):
    return (1 - t)*color1 + t*color2

size = 100
image = np.zeros((size, size, 3), dtype="uint8")
assert image.shape[0] == image.shape[1]

color2 = [255, 128, 0]
color1 = [0, 128, 255] 

for j, t1 in enumerate(np.linspace(0, 1, image.shape[0])):
  for i, t2 in enumerate(np.linspace(0, 1, image.shape[1])):
      r = lerp(color1[0], color2[0], (t2+t1)/2) # (t2+t1)/2 означает, что мы нормируем значение температуры на 1
      g = lerp(color1[1], color2[1], (t2+t1)/2)
      b = lerp(color1[2], color2[2], (t2+t1)/2)
      image[i, j, :] = [r, g, b]

plt.figure(1)
plt.imshow(image)
plt.show()
