class Dec:

    def __call__(self, f):
        print('Dec装饰开始')

        def wrapper(*args, **kwargs):
            print('Dec日志记录中，开始计算...')
            return f(*args, **kwargs)

        return wrapper


def add(a, b):
    res = a + b
    print(f'{a}和{b}相加的结果是{res}')
    return res


print(add(1, 2))
print('*' * 50)
# 手动装饰
obj = Dec()
add_pro = obj.__call__(add)  # 装饰方式1
add_pro2 = obj(add)  # 装饰方式2

print('1' * 50)
print(add_pro(a=1, b=2))
print('2' * 50)
print(add_pro2(a=3, b=4))
print('*' * 50)


# 自动装饰 方式1
@Dec().__call__
def sub(a, b):
    res = a - b
    print(f'{a}和{b}相减的结果是{res}')
    return res


print('*' * 50)
print(sub(1, 2))


# 自动装饰 方式2
@Dec()
def mul(a, b):
    res = a * b
    print(f'{a}和{b}相乘的结果是{res}')
    return res


print('*' * 50)
print(mul(10, 20))


# 带参数的类装饰器
class HasArgs:
    def __init__(self, info):
        self.info = info

    def __call__(self, f):
        print('HasArgs装饰开始')

        def wrapper(*args, **kwargs):
            print(self.info)
            return f(*args, **kwargs)

        return wrapper


print('*' * 50)


# 带参数的类装饰器（比使用嵌套方法实现的方式要简单一些
@HasArgs('Hello，我要开始装饰了')
def div(a, b):
    res = a / b
    print(f'{a}和{b}相除的结果是{res}')
    return res


print('*' * 50)
print(div(20, 5))


# 多个类装饰器的使用

class Deco1:
    def __init__(self):
        print('Deco1 init')

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            print('Deco1 starting')
            return f(*args, **kwargs)

        return wrapper


class Deco2:
    def __init__(self):
        print('Deco2 init')

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            print('Deco2 starting')
            return f(*args, **kwargs)

        return wrapper


print('*' * 50)
@Deco1()
@Deco2()
def mod(a, b):
    res = a % b
    print(f'{a}和{b}取余的结果是{res}')
    return res


print('*' * 50)
print(mod(53, 2))