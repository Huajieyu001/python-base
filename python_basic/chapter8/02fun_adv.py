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
