list1 = [10, 20, 30, 40, 50]
# 需求：获取翻倍列表
# 方式1：map
list2 = list(map(lambda x: x * 2, list1))
print(list2)

# 方式2：使用循环
list3 = []
for item in list1:
    list3.append(item * 2)

print(list3)

# 方式3：列表推导式
list4 = [x * 2 for x in list1]
print(list4)

# 带条件的列表推导式(使用条件表达式）,符合条件的翻倍，不符合的不翻倍
list5 = [x * 2 if x > 20 else x for x in list1]
print(list5)

# 带条件的列表推导式(使用列表推导式的语法）,符合条件的翻倍，不符合的元素被移除
list6 = [x * 2 for x in list1 if x > 20]
print(list6)

# 字典推导式
names = ['Tom', 'Rosy', 'Jack']
scores = [80, 87, 76]

# 字典推导式
dict2 = {k: v for k, v in zip(names, scores)}
print(dict2)
print(dict(zip(names, scores)))  # 效果和上面一样

# 集合推导式
set1 = {1, 2, 3}

set2 = {x * 2 for x in set1}  # 让每个元素翻倍
print(set2)

set1 = {'AAA', 'BBB', 'CCC'}
set2 = {x + '!' for x in set1}  # 在每个元素后面加上感叹号
print(set2)
