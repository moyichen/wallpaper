# !/usr/bin/python3
# -*- coding: utf8 -*-
# author: moyichen
# date:   2021/4/20

import os
import time
import requests
from appscript import app, mactypes
from bs4 import BeautifulSoup


# https://blog.csdn.net/sheldonxxd/article/details/95308411
def download_bing_wallpaper(filepath):
    url = "https://cn.bing.com"
    try:
        r = requests.get(url)
    except:
        print("下载失败，请检查你的网络连接！")
        input("\n请按任意键退出:")
        exit()

    soup = BeautifulSoup(r.text, features="lxml")
    ls = soup.select("link")
    url_img = url + ls[0].attrs["href"]  # 获取图片链接
    jj = ls[0].attrs["href"].split("&")
    j = jj[0].split("=")
    fname = j[1]  # 获取图片文件名
    fjf = soup.select("#sh_cp")
    des = fjf[0].attrs["title"]  # 获取图片描述

    today = time.strftime("%Y-%m-%d")
    today_wallpaper = '{}/{}-{}.jpg'.format(filepath, today, fname)
    with open(today_wallpaper, "wb") as f:
        f.write(requests.get(url_img).content)
    print(fname)
    print(des)
    return today_wallpaper


if __name__ == '__main__':
    today_wallpaper = download_bing_wallpaper(os.path.expanduser('~/wallpaper/images'))
    app('Finder').desktop_picture.set(mactypes.File(today_wallpaper))
