tempSet = set()

tempSet.add('AAA')
tempSet.add('BBB')
tempSet.add('CCC')
tempSet.add('DDD')
tempSet.add('AAA')

print(tempSet)
print(tempSet.add('XXX'))
print(tempSet.remove('AAA'))
print(tempSet)
print(tempSet.pop())
print(tempSet)
print(tempSet.clear())
print(tempSet)

print(type(tempSet))

set2 = {1, True, 'AAA', 97}
print(set2)
print(type(set2))

set3 = frozenset(set2)
print(set3)
print(type(set3))

tempSet = set()

tempSet.add('AAA')
tempSet.add('BBB')
tempSet.add('CCC')
tempSet.add('DDD')
tempSet.add('AAA')

# 移除元素，当元素不存在时就会报错
# tempSet.remove('PPP')
# 移除元素，当元素不存在时不会报错
tempSet.discard('PPP')

print('XXX' in tempSet)
print('AAA' in tempSet)

# common methods

set1 = {'AAA', 'BBB', 'CCC', 'DDD'}
set2 = {'AAA', 'BBB', 'CCC', 'EEE'}
set3 = set1.difference(set2)  # 找出set1中在set2里不存在的元素 'DDD'
print(set3)

set4 = set1.union(set2)  # 合并两个集合
print(set4)

set1.difference_update(set2)  # 删除set1中在set2中能找到的所有元素
print(set1)

set1 = {'AAA', 'BBB', 'CCC', 'DDD'}
set2 = {'AAA', 'BBB', 'CCC'}

print(set1.issubset(set2))  # 判断set1是不是set2的子集
print(set1.issuperset(set2))  # 判断set1是不是set2的父集

set3 = {'XXX'}
set4 = {'SSS'}
print(set3.isdisjoint(set4)) # 判断set3和set4是否没有交集，如果没有则返回True