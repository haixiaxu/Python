"""
example_5 - 列表的相关操作

Author: Hx
Date: 2022/3/21
"""
# 创建列表的方式一: 字面量语法
list1 = ['apple', 'orange', 'pitaya', 'durian']
print(list1)
# 创建列表的方式二: 构造器语法
list2 = list(range(1, 10))
print(list2)
# 创建列表的方式三: 生成式 (推导式) 语法
list3 = [i ** 2 for i in range(1, 10)]
print(list3)

# 获取列表元素的个数 ---> len()
print(len(list1))

# 遍历列表的元素
for index, value in enumerate(list1):
    print(index, value)
print('=' * 30)

for i in list1:
    print(i)
print('=' * 30)

for i in range(len(list1)):
    print(list1[i])
