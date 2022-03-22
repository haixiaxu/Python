"""
example_6 - 显示所有汉子
ord()函数---> 查看字符对应的编码
chr()函数---> 将编码处理成对应的字符

Author: Hx
Date: 2022/3/22
"""

for i in range(0x4e00, 0x9fa6):
    print(chr(i), end='')
