"""
example_21 - 找出1-10000之间的完美数
除自身外所有因子的和等于这个数

Author: jet
Date: 2022/3/15
"""
import time

start = time.time()
for num in range(2, 10000):
    total = 1
    for factor in range(2, int(num ** 0.5) + 1):#range(1,num)
        if num % factor == 0:
            total += factor
            total += num // factor
    if num == total:
        print(num)
end = time.time()
print('执行时间: {0}秒'.format(end - start))
