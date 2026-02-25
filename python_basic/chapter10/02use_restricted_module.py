
from chapter10.demo import *
# 正常使用
say_hello()
# say_goodbye被限制导入
# say_goodbye()

print(var1)
# var2被限制导入
# print(var2)

import named

print(__name__)
print(named.__name__)