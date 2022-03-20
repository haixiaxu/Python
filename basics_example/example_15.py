"""
example_15 - 求阶乘

Author: jet
Date: 2022/3/15
"""
# 从math模块导入factorial函数并别名为f
from math import factorial as f

m = int(input('m='))
n = int(input('n='))
print(f(m) // f(n) // f(m - n))
