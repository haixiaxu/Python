"""
example_7 - 列表的操作 (反转和排序)

Author: Hx
Date: 2022/3/22
"""

items = ['苹果', '香蕉', '西瓜', '苹果', '蓝莓', '芒果']

# 反转
items.reverse()
print(items)

# 排序
print('=' * 50)
# 升序
items.sort()
print(items)
# 降序
items.sort(reverse=True)
print(items)

nums = ['1', '10', '234', '2', '35', '100']
nums.sort(key=int)
print(nums)
# nums2 = [int(num) for num in nums]
# nums2.sort()
# print(nums2)
# nums3 = [str(num) for num in nums]
# print(nums3)
