def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def calc(fun, a, b):
    return fun(a, b)


x = calc(add, 2, 3)
y = calc(sub, 4, 5)
print(x)
print(y)

s = calc(lambda x, y: x * y, 10, 20)
print(s)

# 匿名函数可以复制给变量，可作为普通函数使用
lamf = lambda x, y: x * y
print(lamf(4, 5))