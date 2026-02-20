num: int = 100
print(num)
num = 'hhaha'  # 警告，但不报错，属于一种约定
print(num)
price: float = 5.00
print(price)
message: str = 'welcome to python'
print(message)
message = 'asdf'
print(message)
isMember: bool = True
print(isMember)
list1: list = [1, 2, 3]
print(list1)
tuple1: tuple = (1, 2, 3)
print(tuple1)
dict1: dict = {1: 'one', 2: 'two', 3: 'three'}
print(dict1)
set1: set = {1, 2, 3}
print(set1)
result: None = None
print(result)
result = 1
print(result)

# 也可以先声明但不定义
name: str
# print(name) # 这里会报错，因为上面一行没有定义，只是声明
name = 'Abc'
print(name)

# 也可以定义嵌套类型

hobby: list[str] = [1, 2, 3]  # warn
print(hobby)
hobby = ['game', 'tv', 'ball']
print(hobby)
hobby.append('study')
hobby.append(888)  # warn

# 定义列表，元素可以是str或者int，可以使用管道符
bag: list[str | int] = [1, 2, 3]
print(bag)
bag.append(888)
print(bag)
bag.append('Tom')
print(bag)

# dict
# 定义字典的key为str类型，value为int类型
persons: dict[str, int] = {'one': 1, 'two': 2, 'three': 3}
print(persons)
persons['Tom'] = 4
persons['Rosy'] = 'HJ'  # warn

# tuple 比较特殊，由于元组是不可变的，所以需要一起把所有的元素的类型也给指定
# 因此tuple[str]不行，需要指定为tuple[str, str, str]或者tuple[str, ...]
tuple1: tuple[str, str, str] = ('Haha', 'sadf', 'sdf')
print(tuple1)
tuple2: tuple[str, ...] = ('Haha', 'sadf', 'sdf')
print(tuple2)
# 元素类型定义为str或者int，可以是任意个数
tuple3: tuple[str | int, ...] = ('Haha', 'sadf', 888, 'hello')
print(tuple3)

class Animal:
    pass

# 变量也可以指定类的类型
obj: Animal
obj = 5 # warn
obj = Animal()

# 普通变量：自动推断类型是int，但后续修改不会警告
x = 100
print(x)
x = 'Welcome'
print(x)

# 容器变量：自动推断类型是list[int]，后续修改会警告
list0 = [1, 2, 3]
print(list0)
list0.append('888') # warn
print(list0)