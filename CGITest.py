#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:Liujj 
@file: CGITest.py 
@time: 2018/04/27 
"""
#!/usr/bin/python3

print ("Content-type:text/html")
print ()                             # 空行，告诉服务器结束头部Jetty Liu <Jetty_Liu@on-bright.com>
print ('<html>')
print ('<head>')
print ('<meta charset="utf-8">')
print ('<title>Hello Word - 我的第一个 CGI 程序！</title>')
print ('</head>')
print ('<body>')
print ('<h2>Hello Word! 我是来自菜鸟教程的第一CGI程序</h2>')
print ('</body>')
print ('</html>')