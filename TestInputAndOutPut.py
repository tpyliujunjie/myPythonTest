import  math


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
#可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
print(math.pi)
print('常量 PI 的值近似为 {:.3f}。'.format(math.pi))
#在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {Runoob}; Google: {Google}; Taobao: {Taobao}'.format(**table))
for name, number in table.items():
	print('{0:10} ==> {1:10d}'.format(name, number))
#读取键盘输入
str = input("请输入：")
print ("你输入的内容是: ", str)
# 打开一个文件
f = open("/myPythonTest/my.txt", "w")
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
f.close()
#读文件
f = open("/myPythonTest/hehe.txt", "r","utf-8")
print(f.read())
f.close()