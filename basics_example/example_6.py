"""
example_6 - 输入圆的半径, 计算圆的周长和面积
Author: jet
Date: 2022/3/13
"""
import math

redius = float(input('请输入圆的半径'))
# 周长
perimeter = 2 * math.pi * redius
# 面积
area = math.pi * redius ** 2
print('圆的周长: %s' % perimeter)
print('圆的面积: %s' % area)
