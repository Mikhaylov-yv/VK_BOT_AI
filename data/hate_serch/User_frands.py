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
try:
    friends_1 = vkapi.friends.get(user_id = user_id, v=v)
except:
    e = sys.exc_info()[1]
    print (e)
    sys.exit()
friends_1_count=friends_1['count']
friends_1 =friends_1['items']
def name (usersget):

    #print(data)
    data1 = usersget[0]['first_name']
    # print(data)
    data2 = usersget[0]['last_name']
    # print(data)
    data3 = data1 + ' ' + data2
    reg = re.compile('[^a-zA-Zа-яА-я1-9 ]')
    data3 = reg.sub('', data3)
    return (data3)
friends_1_data = [[],[]]
for i in range(len(friends_1)):
    time.sleep(1 / 3)
    usersget = vkapi.users.get(user_id=friends_1[i], v=v)
    data3 = name(usersget)
    print (usersget[0])
    if data3 != 'DELETED ' and 'deactivated' not in usersget[0]:
        #if usersget[0]['can_access_closed'] == 'True':
        friends_1_data[1].append(data3)
        friends_1_data[0].append(friends_1[i])
print (friends_1_data)


# Запись файла

c = np.column_stack(friends_1_data)
print (c)
FileName = user_id + ' frend.csv'
myFile = open(FileName, 'w', newline='')
with myFile:
    writer = csv.writer(myFile, delimiter=';')
    writer.writerows(c)
