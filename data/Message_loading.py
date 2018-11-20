import vk
import pandas as pd
from io import StringIO
import csv
import time
import datetime
import numpy as np
import re
from my_data import MyVKData_O
v=5.8
session = vk.AuthSession(app_id=MyVKData_O.MY_PRIL_ID, user_login=MyVKData_O.LOGIN, user_password=MyVKData_O.GET_PASSWORD, scope='messages')
vkapi = vk.API(session)
api = vk.API(session, v=5.8)


id = '55370581'
time.sleep(1 / 3)
data = vkapi.users.get(user_id=id, v=v)
data1 = data[0]['first_name']
data2 = data[0]['last_name']
name = data1 + ' ' + data2
us_id = []
messag = []
messag_date = []
message = vkapi.messages.getHistory(user_id = id,count =200, v=v)
message_count = message['count']
print(message)
count = 200

def messagesget(i,message):
    data = message['items'][i]['body']
    reg = re.compile('[^а-яА-я1-9 .!,?:;]')
    data = reg.sub('', data)
    if bool(re.search('[а-яА-я]', message['items'][i2]['body'])):
        messag.append(data)
        data = message['items'][i]['date']
        data = datetime.datetime.fromtimestamp(data)
        messag_date.append(data.strftime('%d-%m-%Y %H:%M:%S'))
        data = message['items'][i]['from_id']
        us_id.append(data)

for i in range((message_count//count)+1):
    time.sleep(1 / 3)
    message = vkapi.messages.getHistory(user_id=id,offset=i*count, count=count, v=v)
    for i2 in range(len(message['items'])):
        messagesget(i2, message)



# Запись файла

c = np.column_stack((us_id, messag, messag_date))
print (c)
FileName = name + ' переписка.csv'
myFile = open(FileName, 'w', newline='')
with myFile:
    writer = csv.writer(myFile, delimiter=';')
    writer.writerows(c)
