#!usr/bin/env python  
#-*- coding:utf-8 _*-
import  os
import glob
import sys
import re
import django
"""
@author:Liujj 
@file: LibraryTest.py 
@time: 2018/04/26 
"""
print('========='+os.getcwd())
#print(help(os))
print(dir(os))
#sys.stderr.write('Warning, log file not found starting a new one\n')
print(glob.glob('*.py'))
print(sys.argv)
str='1234'
str2='23rcsd'
print('title={0}, href={1}'.format('adadad', 1111))
print ("He is %d years old"%(25))
print ("He is %s years old"%('ss'))
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配
#print('title={%s}'.format('adadad'))
print('title={:.2f},'.format(2.1542),'href={0}'.format('222'))