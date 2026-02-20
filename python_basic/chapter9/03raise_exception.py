# 自定义异常
class SelfException(Exception):
    pass

def is_adult(age):
    if age > 200 or age < 0:
        # 手动抛出异常， 类似与java的throw
        raise SelfException('年龄可能是假的')
    elif age >= 18:
        print('teenager')
    else:
        print('children')

is_adult(10)
is_adult(30)
is_adult(300)

