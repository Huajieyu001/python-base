
obj1 = 'AAA'

obj2 = 'BBB'

def caller1():
    print("Ha ha")

def caller2():
    print("Welcome")

# 定义__name__，如果不定义，当前类为启动类时为'__main__'，不为启动类时为模块名，在这里也就是'named'
__name__ = "aaa"

# 这里的语句会在被导入时自动执行
print(f'============', __name__)
