#!usr/bin/env python  
#-*- coding:utf-8 _*-
import pymysql
""" 
@author:Liujj 
@file: TestMysql.py 
@time: 2018/05/02 
"""
db = pymysql.connect("192.168.200.200","admin","im123456","bright_apollo")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)
db.close()

