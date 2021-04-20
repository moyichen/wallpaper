# !/usr/bin/python3
# -*- coding: utf8 -*-
# author: moyichen
# date:   2021/4/20

import os
from appscript import app, mactypes
from wallpaper_bing import download_bing_wallpaper
from wallpaper_momentumdash import download_momentumdash_wallpaper

if __name__ == '__main__':
    # today_wallpaper = download_momentumdash_wallpaper(os.path.expanduser('~/wallpaper/images'))
    today_wallpaper = download_bing_wallpaper(os.path.expanduser('~/wallpaper/images'))
    app('Finder').desktop_picture.set(mactypes.File(today_wallpaper))
