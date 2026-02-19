
tempList = ['AAA', 'BBB', 'CCC', 'DDD', 'AAA', 'XXX', 'SSS', 'CCC']

print(tempList.index('AAA'))
print(type(tempList.index('AAA')))
print(tempList.index('CCC', tempList.index('CCC') + 1))

print('============count===============')
print(tempList.count('CCC'))
print(tempList.count('skuhadfg'))

print('============sort===============')
tempList = [68, 654, 64, 6, 6764, 65, 34]
tempList.sort(reverse=True)
print(tempList)