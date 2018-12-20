import vk
from io import StringIO
import csv
import time
import datetime
import  numpy as np
import re
import httplib2
from my_data import MyVKData_O


def authSession():
    v=5.92
    session = vk.AuthSession(app_id=MyVKData_O.MY_PRIL_ID, user_login=MyVKData_O.LOGIN, user_password=MyVKData_O.GET_PASSWORD, scope='wall, fields, messages')
    vkapi = vk.API(session)
    api = vk.API(session, v=v)
    return vkapi, v


def usersnami_id (user_id):
    time.sleep(1 / 3)
    vkapi = authSession()
    v = vkapi[1]
    vkapi = vkapi[0]
    data = vkapi.users.get(user_id=user_id, v=v)
    data1 = data[0]['first_name']
    data2 = data[0]['last_name']
    user_name = data1 + ' ' + data2
    return user_name

def chat_data(chat_id):
    time.sleep(1 / 3)
    vkapi = authSession()
    v = vkapi[1]
    vkapi = vkapi[0]
    chat=vkapi.messages.getChat(chat_id=chat_id, v=v)
    return chat
def serch(chat_id,csv_path):
    vkapi = authSession ()
    v = vkapi[1]
    vkapi = vkapi[0]
    count = 200
    peer_id = 2000000000 + chat_id
    chat = chat_data(chat_id)
    name = chat['title']
    users = chat['users']
    mem =[[],[],[],[],[]]
    stop = False
    next_from = 0

    dict_user_name ={}

    for i in range(len(users)):
        user_id = users[i]
        user_name = usersnami_id(user_id)
        dict_user_name[user_id] = user_name
    print(dict_user_name)

    while stop == False:
        time.sleep(1 / 3)
        img_data = vkapi.messages.getHistoryAttachments(peer_id = int(peer_id), media_type = 'photo',count = count,start_from=next_from, v=v)
        for i in range(len(img_data['items'])):
            img = img_data['items'][i]['attachment']['photo']
            owner_id = img['owner_id']
            if owner_id not in dict_user_name:
                user_name = usersnami_id(owner_id)
                dict_user_name[owner_id] = user_name
            user_name = dict_user_name[owner_id]
            mem[0].append(user_name)
            sizes_len = len(img['sizes'])-1
            photo = img['sizes'][sizes_len]['url']
            mem[1].append(photo)
            date = img['date']
            mem[3].append(date)
            date = datetime.datetime.fromtimestamp(date)
            mem[2].append(date.strftime('%d-%m-%Y %H:%M:%S'))
            mem[4].append(img_data['items'][i]['message_id'])
        if 'next_from' not in  img_data:
            stop = True
        else: next_from = img_data['next_from']
    print(mem)



    c = np.column_stack((mem))
    print (c)
    FileName = csv_path
    myFile = open(FileName, 'w', newline='')
    with myFile:
        writer = csv.writer(myFile, delimiter=';')
        writer.writerows(c)

def app_mem(csv_path,mem_data):
    mem_data = [[],[],[],[],[]]
    with open(csv_path, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            mem_data[0].append(row[0])
            mem_data[1].append(row[1])
            mem_data[2].append(row[2])
            mem_data[3].append(row[3])
            mem_data[4].append(row[4])