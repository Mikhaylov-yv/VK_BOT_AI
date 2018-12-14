import vk
from io import StringIO
import csv
import time
import re
from my_data import MyVKData_O
import  friends_2
import post_history_fill

v=5.92
session = vk.AuthSession(app_id=MyVKData_O.MY_PRIL_ID, user_login=MyVKData_O.LOGIN, user_password=MyVKData_O.GET_PASSWORD, scope='wall, fields, messages')
vkapi = vk.API(session)
api = vk.API(session, v=v)
group_id = '174909014'
owner_id = '-' + group_id
count = 200

stop = False
while stop == False:
    newsfeed = vkapi.newsfeed.search(q='сдам квартиру', count=count, filters='post ', v=v)
    newsfeed = newsfeed['items']
    post_history = post_history_fill.post_history
    for i in range(len(newsfeed)):
        user_id = newsfeed[i]['from_id']
        post_id = newsfeed[i]['id']
        if user_id in friends_2.a:
            post = 'wall' + str(user_id) + '_' + str(post_id)
            if post not in post_history:
                print ('https://vk.com/id' + str(user_id) + '?w=wall' + str(user_id) + '_' + str(post_id))
                post_history.append(post)
                file = open('post_history_fill.py', 'w')
                file.write('post_history = ' + str(post_history))
                file.close()
                vkapi.messages.send(user_id='255960', attachment=post, group_id=group_id, v=5.0)
    time.sleep(60)