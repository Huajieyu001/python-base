set1 = {'A', 'B', 'C', 'D'}
set2 = {'X', 'S', 'C', 'D'}

print(set1 | set2)  # 并集{'B', 'A', 'C', 'X', 'S', 'D'}
print(set1 & set2)  # 交集{'C', 'D'}
print(set1 - set2)  # 差集{'B', 'A'}
print(set1 ^ set2)  # 对称差集{'B', 'A', 'X', 'S'}，等价于(set1 - set2) | (set2 - set1)，也可以等价为(set1 | set2) - (set1 & set2)
print((set1 - set2) | (set2 - set1))
print((set1 | set2) - (set1 & set2))


for item in set1:
    print(item)
