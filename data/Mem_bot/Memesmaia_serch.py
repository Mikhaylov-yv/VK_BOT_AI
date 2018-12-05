import vk
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


id = '255960'
chat_id = '69'
time.sleep(1 / 3)
chat=vkapi.messages.getChat(chat_id=69, v=v)
name = chat['title']
users = chat['users']

users_names = {}
for i in range(len(users)):
    time.sleep(1 / 3)
    data = vkapi.users.get(user_id=users[i], v=v)
    data1 = data[0]['first_name']
    data2 = data[0]['last_name']
    user_name = data1 + ' ' + data2
    user_id = users[i]
    users_names[user_id]=user_name
print (users_names)

us_id = []
us_name = []
messag = []
messag_date = []
message = vkapi.messages.getHistory(peer_id='20000000'+chat_id,count=1, v=5.65)
message_count = message['count']
message_count = 250
#print(message)
count = 200

def messagesget(i,message):
    data = message['items'][i]['text']
    reg = re.compile('[^a-zA-Zа-яА-я1-9 .!,?:;\/]')
    data = reg.sub('', data)
    if len(message['items'][i]['attachments']) >0:
        if message['items'][i]['attachments'][0]['type']=='photo':
            len_photo = len(message['items'][i]['attachments'][0]['photo']['sizes'])
            photo=message['items'][i]['attachments'][0]['photo']['sizes'][len_photo-1]['url']
            data = photo
    messag.append(data)
    data = message['items'][i]['date']
    data = datetime.datetime.fromtimestamp(data)
    messag_date.append(data.strftime('%d-%m-%Y %H:%M:%S'))
    data = message['items'][i]['from_id']
    us_id.append(data)
    data = users_names[data]
    us_name.append(data)

for i in range((message_count//count)+1):
    time.sleep(1 / 3)
    message = vkapi.messages.getHistory(peer_id='20000000'+chat_id,offset=i*count, count=count, v=6.65)
    for i2 in range(len(message['items'])):
        messagesget(i2, message)



# Запись файла

c = np.column_stack((us_id,us_name, messag, messag_date))
print (c)
FileName = name + ' переписка.csv'
myFile = open(FileName, 'w', newline='')
with myFile:
    writer = csv.writer(myFile, delimiter=';')
    writer.writerows(c)