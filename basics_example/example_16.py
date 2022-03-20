"""
example_16 - 输入一个正整数, 判断他是不是质数(只能被1和自身整除的数)

Author: jet
Date: 2022/3/15
"""
num = int(input('请输入一个正整数: '))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if num > 1 and is_prime:
    print('%s是质数' % num)
else:
    print('%s不是质数' % num)
