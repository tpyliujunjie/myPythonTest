#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:Liujj 
@file: ClassTest.py 
@time: 2018/04/26 
"""
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def prt(self):
	    print(self)
	    print(self.__class__)
x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5
x.prt()


# 类定义
class people:
	# 定义基本属性
	name = ''
	age = 0
	# 定义私有属性,私有属性在类外部无法直接进行访问
	__weight = 0
	# 定义构造方法
	def __init__(self, n, a, w):
		self.name = n
		self.age = a
		self.__weight = w
	
	def speak(self):
		print("%s 说: 我 %d 岁。我的体重%d公斤" % (self.name, self.age,self.__weight))


# 实例化类
p = people('runoob', 10, 30)
p.speak()
#AttributeError: 'people' object has no attribute '__weight'
#__weight is private
#print(p.__weight)
class people:
    def __init__(self,name,age,num):
	    self.age = age
	    self.name = name
	    self.__num = num
	    
    def __str__(self):
        return '这个人的名字是%s,已经有%d岁了%d'%(self.name,self.age,self.__num)
a=people('孙悟空',999,11)
print(a)
