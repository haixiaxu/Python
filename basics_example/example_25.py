"""
example_25 - 输入10次, 0-100的数字, 计算平均值, 最大值, 最小值

Author: jet
Date: 2022/3/18
"""
total = 0
max_value, min_value = 0, 100
for _ in range(10):
    temp = int(input('请输入: '))
    total += temp
    if max_value < temp:
        max_value = temp
    if min_value > temp:
        min_value = temp

print('平均值: {0}'.format(total / 10))
print('最大值: {0}'.format(max_value))
print('最小值: {0}'.format(min_value))
