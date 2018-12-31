import vk

import time
import datetime

from my_data import MyVKData_O
import logging
import sys
v=5.92
session = vk.AuthSession(app_id=MyVKData_O.MY_PRIL_ID, user_login=MyVKData_O.LOGIN, user_password=MyVKData_O.GET_PASSWORD, scope='wall, fields')
vkapi = vk.API(session)
api = vk.API(session, v=5.92)

today = datetime.datetime.today()
friends_1_id = []
friends_1_name = []

friends_2 = []

user_id = '255960'
friends_1 = vkapi.friends.get(user_id = user_id, v=v)
friends_1_count=friends_1['count']
friends_1 =friends_1['items']

friends_1_data = [[],[]]
for i in range(len(friends_1)):
    time.sleep(1 / 3)
    data = vkapi.users.get(user_id=friends_1[i], v=v)
    print(data)
    data1 = data[0]['first_name']
    # print(data)
    data2 = data[0]['last_name']
    # print(data)
    data3 = data1 + ' ' + data2
    friends_1_data[1].append(data3)
    friends_1_data[0].append(friends_1[i])
print (friends_1_data)
#for i in range(len(friends_1)):
for i in range(25):

    try:
        data = friends_1[i]
        friends_1_id.append(data)
        time.sleep(1 / 3)
        data = vkapi.friends.get(user_id=friends_1[i], v=v)
        data = data['items']
        friends_2.append(data)
    except:
        e = sys.exc_info()[1]
        e1 = e.code
        if e1 == 18:
            i=i+1
        else:
            print (e)
            sys.exit()


print (friends_2)
'''
id = '29300929'
print (vkapi.users.get(user_ids = id,fields='deactivated, is_closed, can_access_closed', v=v))
#print (friends_1)
'''
# Запись файла
'''
c = np.column_stack((mem1,likes,my_likes,reposts,mem_date,ocenka))
print (c)
FileName = grup_name + ' переписка.csv'
myFile = open(FileName, 'w', newline='')
with myFile:
    writer = csv.writer(myFile, delimiter=';')
    writer.writerows(c)
'''