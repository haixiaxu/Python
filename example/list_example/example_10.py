"""
example_10 - 随机抽取和乱序

Author: Hx
Date: 2022/3/23
"""
import random

names = ['井柏然', '杨紫', '杨幂', '华晨宇', '黄晨', '过奖', '王进', '李虎']

print(names)

# sample函数可以对列表元素进行无放回抽样
print(random.sample(names, 5))
# choices函数可以对列表元素进行有放回抽样(可以重复抽中)
print(random.choices(names, k=5))
# choice函数可以从列表中随机选择一个元素
print(random.choice(names))
# shuffle函数可以实现列表元素的随机乱序
random.shuffle(names)
print(names)
