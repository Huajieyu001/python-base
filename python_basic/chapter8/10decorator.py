def add(a, b):
    print('start calculating')
    return a + b


def add_mul(a, b, c):
    print('start calculating')
    return a + b + c


# 自定义一个装饰器
def say_hello(caller):
    def wrapper(*args, **kwargs):
        print('你好啊')
        return caller(*args, **kwargs)

    return wrapper


# 手动装饰
add_pro = say_hello(add)

# print(add(1, 2))

print(add_pro(1, 2))

print(add_mul(1, 2, 3))


# 自动装饰
@say_hello
def sub(a, b):
    print('start calculating')
    return a - b


print(sub(1, 2))


# 自定义一个带参数的装饰器
def say_hello_adv(info):
    def outer(caller):
        def wrapper(*args, **kwargs):
            print(info)
            return caller(*args, **kwargs)

        return wrapper

    return outer


@say_hello_adv('starting....')
def mul(a, b):
    print('start calculating')
    return a * b


print(mul(12, 20))

print('-' * 50)

def test1(caller):
    print('test1 working')

    def wrapper(*args, **kwargs):
        print('test1 decorator')
        return caller(*args, **kwargs)

    return wrapper


def test2(caller):
    print('test2 working')

    def wrapper(*args, **kwargs):
        print('test2 decorator')
        return caller(*args, **kwargs)

    return wrapper


# 多个装饰器一起使用
# 会从下往上依次包装（从近到远）
@test1
@test2
def div(a, b):
    print('start calculating')
    return a / b


div(5, 2)
