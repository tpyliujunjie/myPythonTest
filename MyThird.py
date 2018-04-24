#!/usr/bin/env python3

n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))


count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")

languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print (x)
for i in range(0, 10, 3) :
    print(i)
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

print(list(range(5)))

for letter in 'Runoob':  # 第一个实例
    if letter == 'o':  # 字母为 o 时跳过输出
        continue
    print('当前字母 :', letter)

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:  # 变量为 5 时跳过输出
        continue
    print('当前变量值 :', var)
print("Good bye!")


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")

list=[1,2,3,4]
it = iter(list)
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")


vec = [2, 4, 6]
vec1=[3*x for x in vec]
print(vec1)

#矩阵1
matrix=[[1,2,3,4],[11,22,33,44],[21,23,34,43]]
print("矩阵1:",[[row[i] for row in matrix] for i in range(4)])

#矩阵2
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print("矩阵2:",transposed)