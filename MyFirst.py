#!/usr/bin/python3

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')
print ("我叫 %s 今年 %d 岁!\n" % ('小明', 10))
para_str = '''这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
'''
print (para_str)
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]
list1=list1 + [10,11]
print("列表添加",list1)
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
del list2[2]
print ("删除第三个元素 : ", list2)
print(list2[:-2])
list3=[list1,list2]
print(list3[1])
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2=(2,'222')
tup2+=(3,)
print(tup2)
a=2
print(type(a))
a=2.0
print(type(a))
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First','Name':2222}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
dict['Age'] = 8               # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息
print(dict)
cities={
    '北京':{
        '朝阳':['国贸','CBD','天阶','我爱我家','链接地产'],
        '海淀':['圆明园','苏州街','中关村','北京大学'],
        '昌平':['沙河','南口','小汤山',],
        '怀柔':['桃花','梅花','大山'],
        '密云':['密云A','密云B','密云C']
    },
    '河北':{
        '石家庄':['石家庄A','石家庄B','石家庄C','石家庄D','石家庄E'],
        '张家口':['张家口A','张家口B','张家口C'],
        '承德':['承德A','承德B','承德C','承德D']
    }
}
print(cities)
for i in cities['河北']['石家庄']:
    print(i)