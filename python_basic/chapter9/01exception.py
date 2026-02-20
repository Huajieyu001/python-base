# 几种常见异常
# 1.除数不能为0
# ZeroDivisionError: division by zero
# x = 1 / 0
# print(x)


# 2.使用类型不匹配
# TypeError: can only concatenate str (not "int") to str
# y = 'hello' + 5
# print(y)


# 3.使用不存在的属性或者方法
# AttributeError: 'int' object has no attribute 'hahaha'
# z = 10
# print(z.hahaha)


# 4.下标越界
# IndexError: list index out of range
# list1 = [1, 2, 3]
# print(list1[10])


# 5.使用了不存在的变量
# NameError: name 'x' is not defined
# print(x)


# 6.访问了字典中不存在的key
# KeyError: 'hundred'
# dict1 = {'one': 1, 'two': 2, 'three': 3}
# print(dict1['hundred'])


# 7.类型正确但值不合法
# ValueError: invalid literal for int() with base 10: 'abc'
# int('abc')