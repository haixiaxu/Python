"""
example_24 - 数字游戏
随机产生1-100的随机数, 输入自己猜的数字
给出对应的提示: 大一点, 小一点,或恭喜你猜对了,只到猜中
如果猜的次数超过7次,提示智商余额明显不足

Author: jet
Date: 2022/3/18
"""
import random

answer = random.randrange(1, 101)
count = 0
while True:
    count += 1
    num = int(input("请输入数字: "))
    if num < answer:
        print('大一点')
    elif num > answer:
        print('小一点')
    elif answer == num:
        print('恭喜你猜对了')
        break
if count > 7:
    print('智商余额明显不足')
