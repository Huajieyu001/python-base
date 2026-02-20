list1 = [1, 2, 3]

# map会对可迭代对象进行处理然后返回map对象，需要自己转到目标类型
list2 = map(lambda x: x * 2, list1)

print(list1)
print(list2)  # <map object at 0x000001B7DD079540>
print(list(list2))  # [2, 4, 6]

tuple1 = ('python', 'java', 'javascript')
tuple2 = tuple(map(lambda v: v.upper(), tuple1))  # 转换为大写

print(tuple1)
print(tuple2)

print("=" * 30)
# filter 过滤
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = list(filter(lambda v: v > 5, list1))
print(list1)
print(list2)

tuple1 = ('python', 'java', 'javascript')
tuple2 = tuple(filter(lambda v: v != 'java', tuple1))
print(tuple1)
print(tuple2)

names = ['zhangsan', '', 'lust', None, 'Rosy']
print(list(filter(lambda v: v != None and v != '', names)))  # 过滤非法字符串方法1
print(list(filter(lambda v: v, names)))  # 方法二：v如果为空字符或者None就相当于false，这是简写方式

print("*" * 30)
# sorted
list1 = [16, 75, 76, 56, 76, 92, 9821, 451, 4, 2, 485]
print(sorted(list1))
print(list1)

tuple1 = (16, 75, 76, 56, 76, 92, 9821, 451, 4, 2, 485)
print(sorted(tuple1))  # sorted会自动把迭代对象转换成list
print(tuple1)

set1 = {16, 75, 76, 56, 76, 92, 9821, 451, 4, 2, 485}
print(sorted(set1))  # sorted会自动把迭代对象转换成list
print(set1)

# 按照字符串长度排序
names = ['zhangsan', 'AAAAA', 'lus', 'Rosy']
print(sorted(names, key=len))

persons = [
    {'name': '张三', 'age': 10, 'gender': 'male'},
    {'name': '李四', 'age': 20, 'gender': 'male'},
    {'name': '王五', 'age': 18, 'gender': 'male'},
    {'name': '赵六', 'age': 75, 'gender': 'male'},
    {'name': '风清扬', 'age': 80, 'gender': 'male'},
    {'name': '张三丰', 'age': 96, 'gender': 'male'},
    {'name': '杨过', 'age': 24, 'gender': 'male'}
]
# 根据dict的某个属性进行排序
newPersons = sorted(persons, key=lambda x: x['age'])
for value in newPersons:
    print(value)

# reduce
from functools import reduce

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = reduce(lambda oldVal, newVal: newVal + oldVal, list1, 0)
print(result)

strs = ['ab', 'cd', 'ef']
result = reduce(lambda x, y: x + y, strs)  # 字符串拼接
print(result)
