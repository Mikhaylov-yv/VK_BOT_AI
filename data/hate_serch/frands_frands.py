import vk
from io import StringIO
import csv
import time
import datetime
import numpy as np
import re
from my_data import MyVKData_O
import logging
import sys
v=5.92
session = vk.AuthSession(app_id=MyVKData_O.MY_PRIL_ID, user_login=MyVKData_O.LOGIN, user_password=MyVKData_O.GET_PASSWORD, scope='wall, fields')
vkapi = vk.API(session)
api = vk.API(session, v=v)

today = datetime.datetime.today()
user_id = '255960'
csv_path = user_id + ' — test.csv'

friends_1_data = [[],[]]
friends_2_data = [[],[]]
friends_3_data = [[],[]]

with open(csv_path, 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        friends_1_data[0].append(row[0])
        friends_1_data[1].append(row[1])
#print (friends_1_data)
for i in range(10):
#for i in range(len(friends_1_data[0])):
    time.sleep(1 / 3)
    friends_2 = vkapi.friends.get(user_id=friends_1_data[0][i], v=v)['items']
    a=friends_1_data[1][i]
    b = friends_2
    friends_2_data[0].append(friends_1_data[1][i])
    friends_2_data[1].append(friends_2)
print (friends_2_data)

# Запись файла
'''
c = np.column_stack(friends_2_data)
print (c)
FileName = user_id + ' frend_frend.csv'
myFile = open(FileName, 'w', newline='')
with myFile:
    writer = csv.writer(myFile, delimiter=';')
    writer.writerows(c)
'''