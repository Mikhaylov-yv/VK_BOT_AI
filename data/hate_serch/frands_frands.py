import vk
from io import StringIO
import csv
import time
import re
from my_data import MyVKData_O

v=5.92
session = vk.AuthSession(app_id=MyVKData_O.MY_PRIL_ID, user_login=MyVKData_O.LOGIN, user_password=MyVKData_O.GET_PASSWORD, scope='wall, fields')
vkapi = vk.API(session)
api = vk.API(session, v=v)

user_id = '255960'
csv_path = user_id + ' frend.csv'

friends_1_data = [[],[]]
friends_2_data = []
file = open('friends_2.py', 'w')

with open(csv_path, 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        friends_1_data[0].append(row[0])
        friends_1_data[1].append(row[1])
#print (friends_1_data)
for i in range(len(friends_1_data[0])):
    time.sleep(1 / 3)
    friends_2 = vkapi.friends.get(user_id=friends_1_data[0][i], v=v)['items']
    a=friends_1_data[1][i]
    b = friends_2
    friends_2_data.extend(friends_2)
print (len(friends_2_data))
friends_2_data = set(friends_2_data)
print (len(friends_2_data))
#print (friends_2_data)


file.write(str(friends_2_data))
file.close()
