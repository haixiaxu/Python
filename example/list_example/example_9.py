"""
example_9 - 冒泡排序

Author: Hx
Date: 2022/3/23
"""

nums = [35, 12, 99, 58, 67, 42, 49, 31, 73]

for i in range(1, len(nums)):
    for j in range(0, len(nums) - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)
