

tempList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tempTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tempStr = '12345678910'

# 获取子列表list[start, end, stepLength]
print(tempList[1:5:2])
print(tempTuple[1:5:2])

print(tempTuple[1:-1:1])
print(tempTuple[1::1])
print(tempTuple[::-1])
print("================================")

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

list3 = list1 + list2
print(list3)

# list4 = list1 * 2 等价于list4 = list1 + list1
list4 = list1 * 2
print(list4)