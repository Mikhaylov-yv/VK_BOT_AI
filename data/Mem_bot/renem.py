import os
import re

path='photo2'
a = os.listdir(path=path)
for i in range(len(a)):
    data = a[i]
    reg = re.compile('[^a-zA-Z0-9.\/]')
    data = reg.sub('', data)
    os.rename(path + '/' + a[i], path + '/' + data)