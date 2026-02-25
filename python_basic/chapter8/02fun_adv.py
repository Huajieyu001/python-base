# 多返回值时，结果会自动包装为元组
def multiResult(x, y):
    return x + y, x - y


print(multiResult(1, 2))

# 接收多返回值
a, b = multiResult(1, 2)
print(a, b)

# 打包
print('*' * 30)


def pac(*args, **kwargs):
    print(args)
    print(kwargs)


pac(1, 2, 3, k1=111, k2=222)

args = (9, 8, 7)
kargs = {'ka': 999, 'kb': 888}
pac(*args, **kargs)

print('=' * 30)
print(*args)

#
# 条件表达式(相当于三目运算符)          值1 if 布尔表达式 else 值2
a = 1
b = 2
print('aaa' if a > b else 'bbb')
