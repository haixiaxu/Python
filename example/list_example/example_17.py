"""
example_17 - 一个列表中有很多重复元素, 写一段代码去掉列表中的重复元素

Author: Hx
Date: 2022/5/19
"""
items = [15, 12, 12, 15, 12, 35, 47, 45, 35, 12]
unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)
print(unique_items)

# 另一种实现方式, 效率更高一些
print(set(items))

