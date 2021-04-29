# !/usr/bin/python3
# -*- coding: utf8 -*-
# author: moyichen
# date:   2021/4/20

import os
from appscript import app, mactypes
from wallpaper_bing import download_bing_wallpaper
from wallpaper_momentumdash import download_momentumdash_wallpaper

from subprocess import call


# https://www.itranslater.com/qa/details/2583880644157768704
def notification(title, msg):
    cmd = 'ntfy -t \"{}\" send \"{}\"'.format(title, msg)
    os.system(cmd)


# https://apple.stackexchange.com/questions/57412/how-can-i-trigger-a-notification-center-notification-from-an-applescript-or-shel
def notify(msg):
    cmd = 'display notification \"' + msg + '\" with title \"Daily Wallpaper Is Updated\"'
    call(["osascript", "-e", cmd])


if __name__ == '__main__':
    # today_wallpaper = download_momentumdash_wallpaper(os.path.expanduser('~/wallpaper/images'))
    today_wallpaper, description = download_bing_wallpaper(os.path.expanduser('~/wallpaper/images'))
    app('Finder').desktop_picture.set(mactypes.File(today_wallpaper))
    # notify(description)
    notification('Daily Wallpaper Is Updated!', description)
