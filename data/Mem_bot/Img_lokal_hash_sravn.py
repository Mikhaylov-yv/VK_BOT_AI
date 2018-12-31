import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import csv

def dhash(image, hashSize=8):
    # изменить размер входного изображения, добавив один столбец (ширину), чтобы мы
    # можно вычислить горизонтальный градиент
    resized = cv2.resize(image, (hashSize + 1, hashSize))

    # вычислить (относительный) горизонтальный градиент между соседними
    # столбцы пикселей
    diff = resized[:, 1:] > resized[:, :-1]

    # преобразовать разностное изображение в хеш
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

mem_data=[[],[]]

path = 'photo2'
a = os.listdir(path=path)

for i in range(len(a)):
    original_mem_name = a[i]
    mem_name = a[i]
    original_mem = cv2.imread(path + '/' + original_mem_name)
    mem = cv2.imread(path + '/' + mem_name)
    imageHash = dhash(mem)
    mem_data[1].append(original_mem_name)
    mem_data[0].append(imageHash)

c = np.column_stack((mem_data))
print (c)
FileName = 'Хэши.csv'
myFile = open(FileName, 'w', newline='')
with myFile:
    writer = csv.writer(myFile, delimiter=';')
    writer.writerows(c)




