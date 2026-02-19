def welcome(name: int):
    print(f"Welcome to Python!{name}")


welcome('zhangsan')
welcome('lisi')
welcome(18)


def greet(name, gender, age, height):
    print('我是{}, 性别为{}, 年龄是{}岁，身高是{}cm'.format(name, gender, age, height))


# 按照顺序的写法
greet('zhangsan', 'male', '18', '169')
# 不按照顺序的话可以指定参数名称传递
greet(gender='female', name='lisi', height='166', age='18')


def greetAdv(name, gender, /, age, height):
    print('我是{}, 性别为{}, 年龄是{}岁，身高是{}cm'.format(name, gender, age, height))


# greetAdv(gender='female', name='lisi', height='166', age='18')


def greetAdv2(name, gender, *, age, height):
    print('我是{}, 性别为{}, 年龄是{}岁，身高是{}cm'.format(name, gender, age, height))


greetAdv2('zhangsan', 'male', age='18', height='169')


# 默认姓名
def defaultParam(name="默认姓名", gender="未知", age=18, height=183):
    print('我是{}, 性别为{}, 年龄是{}岁，身高是{}cm'.format(name, gender, age, height))


print("*****************")
defaultParam(name="zhangsan")


def availableParams(*args):
    for arg in args:
        print(arg)



def availableParams(*args):
    print(args)
    for arg in args:
        print(arg)

availableParams("sdaaf", 54, "sdfhi", "sdafhiaws")


def availableParams2(**args):
    print(args)
    for arg in args:
        print(arg)

availableParams2(name="sdaaf", age=54, gender="sdfhi", detail="sdafhiaws")


print(None)
print(type(None))


def testR():
    return 100

print(testR())

temp = 100

