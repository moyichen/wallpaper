# !/usr/bin/python3
# -*- coding: utf8 -*-
# author: moyichen
# date:   2021/4/20

import os
import time
import re
import requests
from appscript import app, mactypes


# https://blog.csdn.net/qq_36800514/article/details/103995247
def download_momentumdash_wallpaper(filepath):
    today = time.strftime("%Y-%m-%d")
    client_id = 'aff58215-a36f-4894-9208-e1fa3d4b8d0a'
    url = 'https://api.momentumdash.com/feed/bulk?syncTypes=backgrounds&localDate={localDate}'

    headers = {
        'authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDY2Mzc0OTIuMCwibmJmIjoxNTc1MDE0NzkyLjAsImlzcyI6ImxvZ2luLWFwaS12MiIsInVzZXJfZ3VpZCI6IjVjNjE5N2MxLThkYmYtNGY4MS1iODI3LTIxZTg0ZTA4YzcyZSJ9.hyAjKOjjZW1dfyKXdXkHK1lLDC4Y7xEJvpetnEpCp-M',
        'Host': 'api.momentumdash.com',
        'Accept': '*/*',
        'X-Momentum-ClientId': client_id,
        'x-momentum-clientdate': time.strftime("%Y-%m-%dT%H:%M:%S"),
        'X-Momentum-Version': '0.100.1',
        'x-momentum-settings-etag': '0400bf20-0000-0000-0000-5aaf255a0000',
        'X-Momentum-ClientDate': today,
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Content-Type': 'application/json',
        'cookie': ''
    }

    response = requests.get(url.format(localDate=today), headers=headers).json()
    # print(response)
    backgrounds = response['backgrounds']
    today_uri = backgrounds[0]['filename']
    tomorrow_uri = backgrounds[1]['filename']
    
    # today_uri=https://images.unsplash.com/photo-1506663728000-f68915a9e635?ixlib=rb-0.3.5&q=99&fm=jpg&crop=entropy&cs=tinysrgb&w=2048&fit=max&ixid=eyJhcHBfaWQiOjcwOTV9&s=e4467b100b98dd96d751b2dc331f5fad
    # tomorrow_uri=https://images.unsplash.com/photo-1564858763975-d99de59ee4bb?ixlib=rb-1.2.1&q=99&fm=jpg&crop=entropy&cs=tinysrgb&w=2048&fit=max&ixid=eyJhcHBfaWQiOjcwOTV9
    today_uri = re.sub('&w=\\d+&', '&w=3840&', today_uri)
    tomorrow_uri = re.sub('&w=\\d+&', '&w=3840&', tomorrow_uri)
    
    print('today_uri={today_uri}'.format(today_uri=today_uri))
    print('tomorrow_uri={tomorrow_uri}'.format(tomorrow_uri=tomorrow_uri))
    r = requests.get(today_uri)

    today_wallpaper = '{}/{}.jpg'.format(filepath, today)
    with open(today_wallpaper, 'wb') as f:
        f.write(r.content)
    f.close()
    return today_wallpaper, "NA"


if __name__ == '__main__':
    today_wallpaper, description = download_momentumdash_wallpaper(os.path.expanduser('~/wallpaper/images'))
    app('Finder').desktop_picture.set(mactypes.File(today_wallpaper))
