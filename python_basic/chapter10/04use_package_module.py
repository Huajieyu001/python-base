
# 导入方式6
from trade import order
order.create_order()

# 导入方式7
from trade import pay as zf
zf.alipay()

# 导入方式8（导入在__init__中的方法和属性，不会导入里面没有的东西，也就是说不会直接导入order和pay的东西，如果需要，就得先导入到__init__中）
from trade import *

say_goodbye()

# 导入方式9
# import trade

# 导入子包（方式和上述一样，只不多多了一个层级）
from trade.sub.sub_demo import happy

happy()
