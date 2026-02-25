tempTuple = (1, 54, 54, 635, 1, 54)

print(tempTuple.count(1))
print(tempTuple.index(635))

print(tempTuple[1])
print(sum(tempTuple))

length = len(tempTuple)
print(length)

# 返回的是list而不是tuple
sortedTuple = sorted(tempTuple)
print(sortedTuple)
# 需要自己手动转换
sortedTuple = tuple(sortedTuple)
print(sortedTuple)

emptyTuple = ()
emptyTuple2 = tuple()

print(emptyTuple)
print(emptyTuple2)

print(type(emptyTuple))
print(type(emptyTuple2))

singleTuple = (1,)
print(singleTuple)
print(type(singleTuple))