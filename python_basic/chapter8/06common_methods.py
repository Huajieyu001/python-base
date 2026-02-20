
# print
# print(1, 2, 3, 4, end='ending', sep='\n')
import time

# for i in range(101):
#     print(f'\rloading...{i}%', end='')
#     time.sleep(0.1)

# all and any
list1 = [1, 2, 3, 4, 5, True, False, {15, 54}]
print(all(list1))
print(any(list1))

list1 = []
print(all(list1)) # why it is true ?
print(any(list1))

set1 = {}
print(all(set1))
print(any(set1))

tuple1 = ()
print(all(tuple1))
print(any(tuple1))

# ord and chr
s = '哈'
print(ord(s))
print(chr(97))
