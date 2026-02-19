d1 = {'zhangsan': 18, 'lisi': 24, 'wangwu': 17}

print(d1['lisi'])  # 查：如果不存在就会报错
print(d1.get('lisi2', 'defaultValue'))  # 查：如果不存在也不会报错,还能设置默认值，如果不设置则为None
print(type(d1))

print(d1)
del d1['zhangsan'] # 直接删除
print(d1)
print(d1.pop('lisi'))  # 删除并获取删除的元素的value
print(d1)

print("==================")
print(d1.values())
print(d1.keys())

d1["newKey"] = "value"  # 新增
print(d1)
d1["newKey"] = "value2"  # 修改
print(d1)

print(d1.popitem())

d2 = {'zhangsan': 18, 'lisi': 24, 'wangwu': 17}
d2.update({'haha': 15, 'lisi': 20})  # 增改
print(d2)

for k, v in d2.items():
    print(k, v)

print(d2.items())
print(type(d2.items()))
