import vk_api
import vk
import requests
import random
import time
import datetime
from my_data import MyVKData_O
import Img_srawn_1
import serch_photo
import app_mem

def mem_open(event):
    original_mem = vk.messages.getById(message_ids=event.message_id, extended=1, v=v)['items'][0]['attachments'][0][
        'photo']
    mem_key = list(original_mem.keys())
    mem_key1 = []
    for i in range(len(mem_key)):
        if str(mem_key[i]).startswith('photo_'):
            mem_key1.append(int(str(mem_key[i])[6:len(str(mem_key[i]))]))
    original_mem = original_mem['photo_' + str(mem_key1[len(mem_key1) - 1])]
    return original_mem

v=5.8
session = requests.Session()
login, password = MyVKData_O.LOGIN, MyVKData_O.GET_PASSWORD
vk_session = vk_api.VkApi(login, password, scope='messages, photo')
try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)

chat_id = 1
peer_id = 2000000000  + chat_id

from vk_api.longpoll import VkLongPoll, VkEventType

longpoll = VkLongPoll(vk_session,mode=2)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.attachments:
        if event.from_chat:
            type = event.attachments
            type = list(type.values())
            print(type)
            if 'photo' in type:
                original_mem = mem_open(event)
                random_id = random.randint(0, event.message_id)
                name = serch_photo.chat_data(chat_id)['title']
                csv_path = name + ' все изображения.csv'
                try:
                    file = open(csv_path)
                except IOError as e:
                    serch_photo.serch(chat_id,csv_path)
                repost = Img_srawn_1.baian_detekted(original_mem,csv_path,event.message_id)
                if len(repost)> 0:
                    message = 'Найдено ' + str(len(repost)) + ' баянов'
                    vk.messages.send(peer_id=peer_id, chat_id=chat_id, random_id=random_id,message=message, forward_messages=repost[0], v=6.65)
                else: print('Не баян')
                # Добавить запись в таблицу
                mem_data = [serch_photo.usersnami_id(event.user_id),original_mem,event.datetime.strftime('%d-%m-%Y %H:%M:%S'),event.timestamp,event.message_id]
                app_mem.app(mem_data, csv_path)



