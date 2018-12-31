import cv2
from skimage import io
import numpy as np
import sys

def dhash(image, hashSize=8):
    try:
        # перевести в массив
        image1 = io.imread(image)
        image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        # изменить размер входного изображения, добавив один столбец (ширину), чтобы мы
        # можно вычислить горизонтальный градиент
        resized = cv2.resize(image1, (hashSize + 1, hashSize))
        print(resized)
        # вычислить (относительный) горизонтальный градиент между соседними
        # столбцы пикселей
        diff = resized[:, 1:] > resized[:, :-1]

        # преобразовать разностное изображение в хеш
        mem_hash = sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])
    except:
        e = sys.exc_info()[1]
        e = str(e.args[0])
        print(e[0:6] + ' Error!!! ' + image)
        mem_hash = 'No_hash'
    return mem_hash



