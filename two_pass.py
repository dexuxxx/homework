import numpy as np
import matplotlib.pyplot as plt

def check(image, y, x):
  if not 0 <= x < image.shape[1]:
    return False
  if not 0 <= y < image.shape[0]:
    return False
  if image[y, x] != 0:
    return True
  return False

def neighbours2(image, y, x): # проверка наличия соседей (единички), слева и сверху
  left = y, x-1
  top = y-1, x
  if not check(image, *left):
    left = None
  if not check(image, *top):
    top = None
  return left, top

def find(label, linked):
  j = label
  while linked[j] != 0:
    j = linked[j]
  return j

def union(label1, label2, linked):
  j = find(label1, linked)
  k = find(label2, linked)
  if j != k:
    linked[k] = j

def two_pass_labeling(binary_image):
    labeled = np.zeros_like(binary_image) # массив для меток бинарного изображения
    label = 1 # первая метка
    linked = np.zeros(len(binary_image), dtype='uint') # граф для связки меток
    for y in range(len(binary_image)):
        for x in range(binary_image.shape[0]):
            if binary_image[y, x] != 0:
                # если есть значение в точке, то запоминаем соседей
                # и присваиваем им соответствующие значения меток,
                # иначе переходим к другой метке
                ns = neighbours2(binary_image, y, x)
                if ns[0] is None and ns[1] is None:
                  m = label
                  label += 1
                else:
                  lbs = [labeled[i] for i in ns if i is not None]
                  m = min(lbs) # переменная для связки одного объекта имеющего разные метки
                labeled[y, x] = m
                for n in ns:
                  if n is not None:
                    lb = labeled[n]
                    if lb != m:
                      union(m, lb, linked)
    # print(linked[:20])
    for y in range(binary_image.shape[0]):
      for x in range(binary_image.shape[1]):
        if binary_image[y, x] != 0:
          new_label = find(labeled[y, x], linked)
          if new_label != labeled[y, x]:
            labeled[y, x] = new_label
    return labeled

def count_in_right_way(labeled):
  digit_to_digit = {}
  i = 1
  for y in range(labeled.shape[0]):
    for x in range(labeled.shape[1]):
      if labeled[y, x] in digit_to_digit:
        labeled[y, x] = digit_to_digit[labeled[y, x]]
      elif labeled[y, x] != 0 and labeled[y, x] not in digit_to_digit:
        digit_to_digit.update({labeled[y, x] : i})
        i += 1
  print(digit_to_digit)
  return labeled

if __name__ == "__main__":
    B = np.zeros((20, 20), dtype='int32')
    
    B[1:-1, -2] = 1
    
    B[1, 1:5] = 1
    B[1, 7:12] = 1
    B[2, 1:3] = 1
    B[2, 6:8] = 1
    B[3:4, 1:7] = 1
    
    B[7:11, 11] = 1
    B[7:11, 14] = 1
    B[10:15, 10:15] = 1
    
    B[5:10, 5] = 1
    B[5:10, 6] = 1

    LB = two_pass_labeling(B)
    
    print("Labels - ", list(set(LB.ravel()))[1:])
    
    
    plt.figure(figsize=(12, 5))
    plt.subplot(121)
    plt.imshow(B, cmap="hot")
    plt.colorbar(ticks=range(int(2)))
    plt.axis("off")
    plt.subplot(122)
    plt.imshow(LB.astype("uint8"), cmap="hot")
    plt.colorbar()
    plt.axis("off")
    plt.tight_layout()
    plt.show()