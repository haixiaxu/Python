"""
example_17 - 打印出1-100范围内的质数

Author: jet
Date: 2022/3/15
"""
for num in range(2,100):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if  is_prime:
        print('%s是质数' % num,end=' ')
    # else:
    #     print('%s不是质数' % num)