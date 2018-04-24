import sys

print('命令行参数如下:')
for i in sys.argv:
   print(i)

print('\n\nPython 路径为：', sys.path, '\n')

#  repr() 函数可以转义字符串中的特殊字符
for x in range(1,11):
	print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
	#print(repr(x*x*x).rjust(4))
	