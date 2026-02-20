
var1 = 100

var2 = 200

def say_hello():
    print("Hello World")

def say_goodbye():
    print("Goodbye World")

# 只允许别的地方导入say_hello和var1，其余变量和方法无法通过from xxx import *的方式导入，只能通过具体的方式导入
__all__ = ["say_hello", "var1"]