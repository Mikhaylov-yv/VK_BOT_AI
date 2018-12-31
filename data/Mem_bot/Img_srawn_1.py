import matplotlib.pyplot as plt
import numpy as np
import cv2
import csv
import os
import httplib2
from skimage import io


def mse(imageA, imageB):

    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    return err

def compare_images(imageA, imageB):
    # вычислить среднеквадратическую ошибку и структурное сходство
    # индекс для изображений
    m = mse(imageA, imageB)
    return m

def sravnenie(original_mem, mem,original_mem_name,mem_name):
        # конвертировать изображения в оттенки серого
        original_mem = cv2.cvtColor(original_mem, cv2.COLOR_BGR2GRAY)
        mem = cv2.cvtColor(mem, cv2.COLOR_BGR2GRAY)

        # сравнить изображения
        original_mem_name = original_mem_name.split('.', 1)[0]
        mem_name = mem_name.split('.', 1)[0]
        baian_name = "original_mem vs. mem " + original_mem_name + ' ' + mem_name
        delta = compare_images(original_mem, mem)
        print(int(delta))
        baian = False
        if int(delta) < 1000:
            baian = True
        return baian

def baian_detekted(original_mem_name, csv_path,message_id):
    mem_data = [[], [],[]]

    with open(csv_path, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row  in reader:
                mem_data[0].append(row [1])
                mem_data[1].append(row [4])
    f.close()


    a = mem_data[0]
    baian = False
    baians_id = []
    for i2 in range(len(a)):
        mem_name = a[i2]
        original_mem = io.imread(original_mem_name)
        mem = io.imread(mem_name)

        if message_id != mem_data[1][i2]:
            if original_mem.shape == mem.shape:
                baian = sravnenie(original_mem, mem,original_mem_name,mem_name)
            elif original_mem.shape[0]/original_mem.shape[1] == mem.shape[0]/mem.shape[1]:
                sootn = original_mem.shape[0] / mem.shape[0]
                mem = cv2.resize(mem, (0,0), fx=sootn, fy=sootn)
                baian = sravnenie(original_mem, mem, original_mem_name, mem_name)
            if baian == True:
                baians_id.append(mem_data[1][i2])

    return baians_id

    '''
            else:
                sootn_x = original_mem.shape[0] / mem.shape[0]
                sootn_y = original_mem.shape[1] / mem.shape[1]
                if sootn_y>sootn_x:
                    mem = cv2.resize(mem, (0, 0), fx=sootn_y, fy=sootn_y)
                else:
                    mem = cv2.resize(mem, (0, 0), fx=sootn_x, fy=sootn_x)
    
                x = original_mem.shape[0] - mem.shape[0]
                y = original_mem.shape[1] - mem.shape[1]
                mem_crop = mem[0:0+original_mem.shape[0], 0:0+original_mem.shape[1]]
                sravnenie(original_mem, mem_crop, original_mem_name, mem_name, path)
    '''
