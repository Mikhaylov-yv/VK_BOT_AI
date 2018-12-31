import matplotlib.pyplot as plt
import numpy as np
import cv2
import csv
import os
import httplib2
from skimage import io
import mem_hash

def baian_detekted(original_mem_name, csv_path,message_id):
    mem_data = [[], [],[]]

    with open(csv_path, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row  in reader:
                mem_data[0].append(row [1])
                mem_data[1].append(row [4])
                mem_data[2].append(str(row[5]))
    f.close()

    baians_id = []
    original_mem_hash = mem_hash.dhash(original_mem_name)
    for i in range(len(mem_data[0])):
        if message_id != mem_data[1][i] and mem_data[2][i] != 'No_hash':
            if original_mem_hash == int(mem_data[2][i]):
                baians_id.append(mem_data[1][i])

    return baians_id

