"""
example_8 - 排序
简单选择排序 - 每次从剩下的元素中选择最小
Author: Hx
Date: 2022/3/22
"""

nums = [35, 12, 56, 88, 56, 45, 49, 31, 21]
nums.sort()
sorted_nums = []
while len(nums) > 0:
    min_value = min(nums)
    sorted_nums.append(min_value)
    nums.remove(min_value)
print(nums)
print(sorted_nums)

print('=' * 50)

nums2 = [35, 12, 56, 88, 56, 45, 49, 31, 21]
for i in range(len(nums2) - 1):
    # 假设第一个元素就是最小值
    min_value, min_index = nums2[i], i
    # 通过循环寻找有没有更小的值, 并记下它的位置
    for j in range(i + 1, len(nums2)):
        if nums2[j] < min_value:
            min_index = j
            min_value = nums2[j]
    # 将最小的值换到最前面位置
    nums2[i], nums2[min_index] = nums2[min_index], nums2[i]
print(nums2)
