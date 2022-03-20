"""
example_2 - 将一颗骰子, 掷60000次, 统计每一面出现的次数

Author: Hx
Date: 2022/3/20
"""
import random

fs = [0] * 6
for _ in range(60000):
    face = random.randrange(1, 7)
    fs[face - 1] += 1
print(fs)

for i, value in enumerate(fs):
    print('{0}点摇出了{1}次'.format(i + 1, value))
