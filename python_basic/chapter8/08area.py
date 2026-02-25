
a = 100


def test():
    c = 100
    print(c, 'at test before inner')
    def inner():
        nonlocal c
        c = 200
        global a
        a = 888
        print(c, 'at inner')

    inner()
    print(c, 'at test after inner')


test()
print(a)