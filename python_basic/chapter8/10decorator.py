def add(a, b):
    print('start calculating')
    return a + b


def add_mul(a, b, c):
    print('start calculating')
    return a + b + c


# 自定义一个装饰器
def say_hello(caller, info):
    def wrapper(*args, **kwargs):
        print(info)
        return caller(*args, **kwargs)

    return wrapper


add_pro = say_hello(add, '你好啊')

# print(add(1, 2))

print(add_pro(1, 2))

print(add_mul(1, 2, 3))
