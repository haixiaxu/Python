"""
example_8 - 分段函数求值

Author: jet0

Date: 2022/3/13
"""
x = float(input('x='))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(x) = %s' % y)
