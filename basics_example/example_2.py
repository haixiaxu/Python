# -- coding: utf-8 --
# author：Hx time:2022/3/12
"""
example_2 - 格式化输出

Author: jet
Date: 2022/3/12
"""

a1 = float(input('a='))
b1 = float(input('b1='))

print('%f + %f = %f' % (a1,b1,a1 + b1))
# print(f'{a1}+{b1}={a1+b1}')

print('%f - %f = %f' % (a1,b1,1 - b1))
print('%f * %f = %f' % (a1, b1, a1 * b1))
print('%f / %f = %f' % (a1, b1, a1 / b1))
print('%f // %f = %f' % (a1, b1, a1 // b1))
print('%f %% %f = %f' % (a1, b1, a1 % b1))
print('%f ** %f = %f' % (a1, b1, a1 ** b1))
