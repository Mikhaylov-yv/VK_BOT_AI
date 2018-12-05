import vk
from io import StringIO
import csv
import time
import datetime
import numpy as np
import re
from my_data import MyVKData_O
v=5.8
session = vk.AuthSession(app_id=MyVKData_O.MY_PRIL_ID, user_login=MyVKData_O.LOGIN, user_password=MyVKData_O.GET_PASSWORD, scope='wall')
vkapi = vk.API(session)
api = vk.API(session, v=5.8)

today = datetime.datetime.today()

grup_id = '30022666'
grup_id_ = '-'+grup_id
grup_data = vkapi.groups.getById(group_ids=grup_id,fields='members_count' ,v=v)
grup_name = grup_data[0]['name']
members_count = grup_data[0]['members_count']
mem1 = []
likes = []
my_likes=[]
mem_date=[]
reposts=[]
ocenka=[]

mem=vkapi.wall.get(owner_id= grup_id_,v=v,limit=1)
wall_count=mem['count']
count=200

def swez_mem (today,time_):
    mem_date = datetime.datetime.fromtimestamp(time_)
    time_ = today - mem_date
    time_days = time_.days
    return time_days

def swez_mem_min (today,time_):
    mem_date = datetime.datetime.fromtimestamp(time_)
    time_ = today - mem_date
    time_min = time_.seconds//60 + time_.days*24*60
    return time_min

def wallget(i,mem):
    data = mem['items'][i]['text']
    reg = re.compile('[^a-zA-Zа-яА-я1-9 .!,?:;\/]')
    data = reg.sub('', data)
    if len(mem['items'][i]['attachments']) >0:
        if mem['items'][i]['attachments'][0]['type']=='photo':
            # Не работает поиск фото нужного качества
            #a = mem['items'][i]['attachments'][0]['photo']['sizes']
            #len_photo = len(mem['items'][i]['attachments'][0]['photo']['sizes'])
            #photo=mem['items'][i]['attachments'][0]['photo']['sizes'][len_photo-1]['url']
            a = mem['items'][i]['attachments'][0]['photo']
            from collections import defaultdict
            v = defaultdict(list)
            for key, value in sorted(a.iteritems()):
                v[value].append(key)

            #a = a.keys()

            print (a[1])
            for i in range(len(a)):
                if re.search(r'photo',a([i])):
                    a.remove(i)
            print (a)
            photo = mem['items'][i]['attachments'][0]['photo']['photo_130']
            data = photo

    mem1.append(data)
    data_likes = mem['items'][i]['likes']['count']
    likes.append(data_likes)
    data = mem['items'][i]['likes']['user_likes']
    my_likes.append(data)
    time_ = mem['items'][i]['date']
    data_time = swez_mem_min(today, time_)
    mem_date.append(data_time)
    data = mem['items'][i]['reposts']['count']
    reposts.append(data)
    data = data_likes/data_time/members_count*10000
    ocenka.append(data)
i = 0
while i in range(len(mem['items'])) and 'is_pinned' in mem['items'][i]:
    i=i+1
time_= mem['items'][1]['date']
#Проблемы с закрепленным постом слишком старый
while i in range((wall_count//count)+1) and swez_mem(today,time_)<1:
    time.sleep(1 / 3)
    mem = vkapi.wall.get(owner_id=grup_id_, v=v,count=count, offset=i)
    time_ = mem['items'][0]['date']
    i2=0
    while i2 in range(len(mem['items'])) and swez_mem(today, time_) < 1:
        time_ = mem['items'][i2]['date']
        wallget(i2, mem)
        i2 = i2 + 1
    i=i+1
#print (grup_data)


# Запись файла

c = np.column_stack((mem1,likes,my_likes,reposts,mem_date,ocenka))
print (c)
FileName = grup_name + ' переписка.csv'
myFile = open(FileName, 'w', newline='')
with myFile:
    writer = csv.writer(myFile, delimiter=';')
    writer.writerows(c)
