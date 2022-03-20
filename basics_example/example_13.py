"""
example_13 - 找出100-999之前的水仙花数

Author: jet
Date: 2022/3/14
"""
for num in range(100, 1000):
    bw = num // 100
    sw = num // 10 % 10
    gw = num % 10
    if bw ** 3 + sw ** 3 + gw ** 3 == num:
        print(num)
