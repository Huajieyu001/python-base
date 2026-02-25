# list
tempList = [1, 2, 3]

print(tempList)
print(type(tempList))

# tuple
tempTuple = (1, 2, 3)
print(tempTuple)
print(type(tempTuple))

# index
tempList = ['AAA', 'BBB', 'CCC']
print(tempList[0])
print(tempList[-1])

# crud
print("===========crud==========")
tempList.append('DDD')
print(tempList)
tempList.append('CCC')
print(tempList)
tempList.insert(1, 'SSS')
print(tempList)
tempList.remove('CCC')  # 如果有多个CCC，那么就只会删除第一个
print(tempList)
tempList[2] = 'XXX'
print(tempList)
tempList.reverse()
print(tempList)
tempList.pop()
print(tempList)

list2 = [1, 2, 3]
tempList.extend(list2)
print(tempList)

del tempList[4]
print(tempList)
del tempList[4]
print(tempList)
del tempList[4]
print(tempList)

tempList.clear()
print(tempList)
