#!/bin/sh

# 记录一下开始时间
echo `date` >> ./log.txt &&
# 执行python脚本（注意前面要指定python运行环境/usr/bin/python，根据自己的情况改变）
python3 ./launch.py
# 运行完成
echo 'finish' >> ./log.txt
