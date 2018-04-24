x=10*3.25
y=200*200
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
print(s)
#  repr() 函数可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
print(hello)
hellos = repr(hello)
print(hellos)
print(repr((x, y, ('Google', 'Runoob'))))
print('这里有两种方式输出一个平方与立方的表:第一种方式')
#这里有两种方式输出一个平方与立方的表:
for x in range(1, 11):
	print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
	print(repr(x * x * x).rjust(4))
print('第二种方式:\n')
for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
#另一个方法 zfill(), 它会在数字的左边填充 0，如下所示：
print('12'.zfill(5))
print('-1.12'.zfill(8))
#format使用方法
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob',other='Taobao'))