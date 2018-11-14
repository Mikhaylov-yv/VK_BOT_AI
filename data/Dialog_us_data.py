import vk
import pandas as pd
from io import StringIO
import csv
import time
import datetime
import numpy as np
from my_data import MyVKData_O
v=5.8
session = vk.AuthSession(app_id=MyVKData_O.MY_PRIL_ID, user_login=MyVKData_O.LOGIN, user_password=MyVKData_O.GET_PASSWORD, scope='messages')
vkapi = vk.API(session)
api = vk.API(session, v=5.8)
dialog_id = []
dialog_type = []
count_messag = []
name = []
sex = []
bdate = []
us_id = []

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
#print(df)
#print(id) # список ид пользователь с диалогами у меня
count_id=id.size
time.sleep(1/3)
for i in range(count_id):
    time.sleep(1/3)
    data= int(vkapi.messages.getHistory(user_id = id[i],v=v)['count'])
    count_messag.append(data)
    print(count_messag)
    time.sleep(1 / 3)
    data = vkapi.users.get(user_id=id[i],fields=('bdate','sex'), v=v)
    print(data)
    data1 = data[0]['first_name']
    #print(data)
    data2 = data[0]['last_name']
    #print(data)
    data3 = data1 + ' ' + data2

    print (type(data3))
    name.append(data3)
    data4 = data[0]['id']
    us_id.append(data4)
    print (us_id)
    if 'sex' in data[0]:
        data1 = data[0]['sex']
    else:
        data1 = ''
    sex.append(data1)
    if 'bdate' in data[0]:
        data2 = data[0]['bdate']
    else:
        data2 = ''
    bdate.append(data2)
'''
df1 = pd.DataFrame(us_id, columns=['us_id'])
df2 = pd.DataFrame(name, columns=['name'])
df3 = pd.DataFrame(count_messag, columns=['count_messag'])
df4 = pd.DataFrame(sex, columns=['sex'])
df5 = pd.DataFrame(bdate, columns=['bdate'])
print (df4)
df = pd.concat([df1, df2, df3, df4, df5], axis=1)
print (df)

FileName =  'Dialog_data.csv'
myFile = open(FileName, 'w',newline='')
df.to_csv(FileName, sep = ';')
'''
c = np.column_stack((us_id, name, count_messag,sex,bdate))
#print(c)
FileName =  'Dialog_data.csv'
myFile = open(FileName, 'w',newline='')
with myFile:
    writer = csv.writer(myFile,delimiter=';')
    writer.writerows(c)

