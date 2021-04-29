#!/bin/sh

CURPATH=$(cd "$(dirname "$0")"; pwd)
cd $CURPATH

# 记录一下开始时间
echo `date` >> ./log.txt &&
# 执行python脚本（注意前面要指定python运行环境/usr/bin/python，根据自己的情况改变）
/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 ./launch.py
# 运行完成
echo 'finish' >> ./log.txt
