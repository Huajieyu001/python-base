def outer():
    num = 10

    def inner():
        print(num)

    return inner


outer() # 会返回inner
outer()() # 会调用inner
