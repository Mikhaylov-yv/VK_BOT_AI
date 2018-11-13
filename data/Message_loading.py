import vk
import pandas as pd
from io import StringIO
import csv
import time
import datetime
import numpy as np
from my_data import MyVKData
v=5.8
session = vk.AuthSession(app_id=MyVKData.MY_PRIL_ID, user_login=MyVKData.LOGIN, user_password=MyVKData.GET_PASSWORD, scope='messages')
vkapi = vk.API(session)
api = vk.API(session, v=5.8)
dialog_id = []
dialog_type = []
dialog_count = vkapi.messages.getConversations(v=v)['count']
time.sleep(1/3)
print(dialog_count//200)
count = 200
for i in range((dialog_count//count)+1):
    all_dialog= vkapi.messages.getConversations(v=v, count = count,offset = (i*count))#['items'][0]['conversation']['peer']
    #count = dialog_count - i
    #print(all_dialog)
    time.sleep(1/3)
    if i >= dialog_count//count:
        count = dialog_count - count*i
    for i in range(count):
        data = all_dialog['items'][i]['conversation']['peer']['id']
        dialog_id.append(data)
        data = all_dialog['items'][i]['conversation']['peer']['type']
        dialog_type.append(data)
dialog_id = np.array(dialog_id)
dialog_type = np.array(dialog_type)
#d = dict(zip(dialog_type,dialog_id))
#print(d)
#print(d.get('user'))
dialog = np.vstack((dialog_id, dialog_type))
print(dialog)
df1 = pd.DataFrame(dialog_id, columns=['id'])
df2 = pd.DataFrame(dialog_type, columns=['dialog_type'])
df = pd.concat([df1, df2], axis=1)
df = df[df['dialog_type'] == 'user']
id = np.array(df['id'].tolist())
print(df)
print(id) # список ид пользователь с диалогами у меня
count_id=id.size
time.sleep(1/3)
print(vkapi.messages.getHistory(user_id = '49440451',v=v)['count'])
#for i in range(count_id):
    #time.sleep(1/3)
    #count_messag= vkapi.messages.getHistory(user_id = id[i],v=v)



