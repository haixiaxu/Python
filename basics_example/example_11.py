"""
example_11 - 计算输出最大公约数

Author: jet
Date: 2022/3/14
"""
x = int(input('x='))
y = int(input('y='))

# for i in range(x, 0, -1):
#     if x % i == 0 and y % i == 0:
#         print(i)
#         break
while y % x != 0:
    x, y = y % x, x
print(x)
