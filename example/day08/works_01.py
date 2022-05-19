"""
example_01 - 一个列表中有很多重复元素, 写一段代码去掉列表中的重复元素

Author: Hx
Date: 2022/5/19
"""

items = [10, 12, 10, 12, 15, 10, 15, 12, 35, 88, 35, 56, 88, 56]
unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)
print(unique_items)

# 另一种实现方式
print(set(items))
