"""
example_14 - 输入一个正整数N, 将N进行翻转
Author: jet
Date: 2022/3/14
"""
n = int(input('请输入正整数'))
total = 0
while n > 0:
    total = total * 10 + n % 10
    n //= 10
print(total)

