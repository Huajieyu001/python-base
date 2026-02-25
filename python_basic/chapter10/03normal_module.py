
import copy
import os
import random
import time
import math
import sys

# 前三个是非内置模块（使用python编写）
print(copy.__file__)
print(os.__file__)
print(random.__file__)
# 后三个是内置模块（使用c编写）,无法通过__file__获取到位置
print(time.__file__)
print(math.__file__)
print(sys.__file__)