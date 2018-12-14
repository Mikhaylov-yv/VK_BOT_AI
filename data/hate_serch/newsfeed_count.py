import vk
from io import StringIO
import csv
import time
import re
from my_data import MyVKData
import  friends_2

v=5.92
session = vk.AuthSession(app_id=MyVKData.MY_PRIL_ID, user_login=MyVKData.LOGIN, user_password=MyVKData.GET_PASSWORD, scope='wall, fields, messages')
vkapi = vk.API(session)
api = vk.API(session, v=v)
count = 200

stop = False
first_post = ''
while stop == False:
    newsfeed = vkapi.newsfeed.search(q='горы', count=count, filters='post ', v=v)
    newsfeed = newsfeed['items']
    #last_post = newsfeed[len(newsfeed)-1]
    if first_post in newsfeed:
        print (newsfeed.index(first_post))
        if first_post != '':
            print ('https://vk.com/id' + str(user_id) + '?w=wall' + str(user_id) + '_' + str(post_id))
    else:
        print ('Отсутствует')
        if first_post!= '':
            print ('https://vk.com/id' + str(user_id) + '?w=wall' + str(user_id) + '_' + str(post_id))

    first_post = newsfeed[0]
    user_id = newsfeed[0]['from_id']
    post_id = newsfeed[0]['id']

    time.sleep(60)