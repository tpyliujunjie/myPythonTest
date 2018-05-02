#!usr/bin/env python  
#-*- coding:utf-8 _*-
import socket
import sys
""" 
@author:Liujj 
@file: SocketClient.py 
@time: 2018/05/02 
"""
# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口好
port = 9999

# 连接服务，指定主机和端口
s.connect(('192.168.200.198', port))

# 接收小于 1024 字节的数据
msg = s.recv(1024)

s.close()

print (msg.decode('utf-8'))