#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:Liujj 
@file: FileTest.py 
@time: 2018/04/25 
"""
#file=open('/myPythonTest/test','a+')
#file.write('hello world\n,hehhehehe\n,hahahahha\n')
#file.flush()
file=open('/myPythonTest/test','r')
#print(file.readline())
print(file.readlines(6))
print(file.readlines(6))
print(file.readlines(1))
print(file.readlines(3))
print(file.readlines(4))
print(file.readlines(2))
print(file.readlines(6))
file.close()
