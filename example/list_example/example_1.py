"""
example_1 - 列表的遍历, 把每个元素输出

Author: jet
Date: 2022/3/20
"""
# 对列表进行读写的操作
nums = [23, 34, 46, 57, 68, 79]
for i in range(len(nums)):
    print(nums[i])
    # nums[i]=100
    # print(nums[i])

print()
print('=' * 30)

# 对列表进行读操作的for循环
for num in nums:
    print(num, end='\t')

print()
print('=' * 30)
for i, x in enumerate(nums):
    print(i, x)
