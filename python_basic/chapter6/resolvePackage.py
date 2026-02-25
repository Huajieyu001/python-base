tempList = [1, 2, 3]
tempTuple = tuple(tempList)


def fun(*args):
    print(args)
    print(type(args))


fun(*tempTuple)


def fun2(a, b, c):
    print(a, b, c)


# 自动把元组进行拆分分配给3个参数
fun2(*tempTuple)
