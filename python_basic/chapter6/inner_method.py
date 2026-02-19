

tempList = [654, 65, 45, 4254, 312, 54, 58, 324]

newList = sorted(tempList, reverse=True)
print(newList)

# get length
print(tempList.__len__())
print(len(tempList))

print(max(tempList))
print(min(tempList))
print(sum(tempList))

# foreach
print("=================================foreach")
for item in tempList:
    print(item)

print("=================================foreach and get index")
for index, item in enumerate(tempList):
    print(index, item)

print("=================================foreach and get index22222")
# start代表index的起始值，不写默认为0，假设原本是0-7，现在变成了5-12，依然会遍历完7个元素
for index, item in enumerate(tempList, start=5):
    print(index, item)