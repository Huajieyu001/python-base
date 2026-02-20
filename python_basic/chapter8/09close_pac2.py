def outer():
    num = 10

    def inner():
        nonlocal num
        num += 1
        print(num)

    return inner


f = outer()
f()
f()
f()
# 输出结果如下，说明outer和num并没有被销毁，而是被保留了下来
# 11
# 12
# 13

# 如果使用
outer()()
outer()()
outer()()
# 调用，那么每次都返回11

f() # 14

# 查看闭包单元，能够看到救下来的cell
print(f.__closure__)
print(outer().__closure__)

# 获取具体闭包的值
print(f.__closure__[0].cell_contents)

# 尝试kill f
f = None
