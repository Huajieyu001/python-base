import copy

list1 = [1, 2, 3, 4]
list2 = list1 # 浅拷贝，直接复制内存地址
list3 = copy.copy(list1) # 表层深拷贝，内部还是浅拷贝，等价于list.copy()
list4 = copy.deepcopy(list1) # 浅拷贝

print(list2)
print(list3)
print(list4)
print(id(list1))
print(id(list2))
print(id(list3))
print(id(list4))

list1[0] = 888 # 只影响list2
print(list2)
print(list3)
print(list4)

print('*' * 50)
list1 = [['aaa', 'bbb'], ['ccc', 'ddd'], ['eee', 'fff']]
list2 = copy.copy(list1)
list3 = copy.deepcopy(list1)
list4 = list1.copy()

print(list1)
print(list2)
print(list3)
print(list4)

list1[0][0] = 'xxx'
print(list1)
print(list2)
print(list3)
print(list4)

