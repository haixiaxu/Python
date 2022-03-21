"""
example_4 - 向列表中添加10个随机数, 找出其中第2个的元素

Author: Hx
Date: 2022/3/21
"""
import random

# 列表的生成式 (推导式) --->写法简明, 效率更高
nums = [random.randrange(1, 100) for _ in range(10)]
# nums = [i for i in range(1, 100, 2)]
# for _ in range(10):
#     temp = random.randrange(1, 100)
#     nums.append(temp)
print(nums)
# 先找出最大值
max_value = max(nums)
# 通过remove操作, 从列表中删除指定元素
nums.remove(max_value)
# 再找最大值, 就是第二大
print(max(nums))

print('=' * 30)

# 另外一种方法实现
nums = [98, 45, 66, 99, 87, 99, 78, 41, 63]
m1, m2 = nums[0], nums[1]
for i in range(2, len(nums)):
    if nums[i] > m1:
        m1, m2 = nums[i], m1
    elif nums[i] == m1:
        pass
    elif nums[i] > m2:
        m = nums[1]
print(nums)
print(m1, m2)
