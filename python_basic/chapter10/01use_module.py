
import order #引入方式1
import pay as paying# 引入方式2
from chapter10.pay import alipay # 引入方式3
from chapter10.pay import alipay as default_pay # 引入方式4
from chapter10.pay import * # 引入方式5

order.create_order()
paying.wechat_pay()

alipay()
default_pay()

print(max_timeout)