def fun():
    print('hello world')


# 1.函数也是对象，可以赋值给别的对象
s = fun

print(s)
print(type(s))

# 2.给函数添加属性
fun.version = 1
fun.desc = 'test method'
print(fun.version)
print(fun.desc)

print(s.version)  # 也是可以访问


def caller(func):
    print("caller is invoked!")
    func()


def funM():
    print('hello world')


# 函数也可以作为参数
caller(funM)
