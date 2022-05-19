"""
example_02 - 有一个放整数的列表, 找出列表中出现次数最多的元素

Author: Hx
Date: 2022/5/19
"""
nums = [10, 10, 1, 1, 10, 100, 100, 1, 10, 1, 1, 10]
# 假设nums[0]是出现次数最多的
items, max_counter = [nums[0]], nums.count(nums[0])

# 切片, 从第2位开始循环
for num in nums[1:]:
    curr_counter = nums.count(num)
    if curr_counter > max_counter:
        items.clear()
        items.append()
        max_counter = curr_counter
    elif curr_counter == max_counter:
        if num not in items:
            items.append(num)

for item in items:
    print(item)
