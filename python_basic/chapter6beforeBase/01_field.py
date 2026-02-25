"""
@author:Huajieyu
@file: chapter6beforeBase.py
@description: test a python file
"""

name = 'zhangsan'
age = 18
weight = 70.2
info = '我是%.1s，年龄是%.3i，体重是%2.1f'%(name,age,weight)
print(info)

print('AAA')
print('AAA\rCCC')
print('BBB')

print(type(int(84.654)))
print(type(float(12)))
print(type(int('   69262     ')))

print(9 // 2)

print(type(False))

print(bool(0))
print(bool(1))

print(bool(2000))
print(bool('0'))
print(bool(12.534))
print(bool(-1))

print(True and False)
print(True or False)
print(not True)

numb = 0b11001
numo = 0o1034
numh = 0x1cf
b = 1 + numb
print(numb)
print(numo)
print(numh)
print(b)

# 把十进制转成二进制，八进制和十六进制
print(bin(25))
print(oct(540))
print(hex(463))

print(int('0b11001', 2))

