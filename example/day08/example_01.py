"""
example_01 - 字符串运算

Author: Hx
Date: 2022/5/19
"""
a = 'HelloKitty'

# 获取字符串的长度
print(len(a))

# 循环变量字符串的每个字符
for i in range(len(a)):
    print(a[i])

print('=' * 50)

for i in a:
    print(i)

# 重复
print(a * 5)

# 成员运算
print('or' in a)
print('ko' in a)

b = 'hello, world'
# 比较运算(比较字符串的内容---> 字符编码大小)
print(a == b)
print(a != b)

c = 'goodbye, world'
print(b > c)

d = 'hello, everybody'
print(b >= c)

# ord查看字符编码大小
print(ord('W'), ord('c'))
