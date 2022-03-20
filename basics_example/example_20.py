"""
example_20 - 输入三角形三条边的长度, 如果嫩构成三角形就计算周长和面积
如果不能构成三角形, 提示用户已重新输入,  直到正确

Author: jet
Date: 2022/3/15
"""
import math
while True:
    a = float(input('a='))
    b = float(input('b='))
    c = float(input('c='))
    if a + b > c and b + c > a and a + c > b:
        perimeter = a + b + c
        half = perimeter / 2
        # 海伦公式
        area = math.sqrt(half * (half - a) * (half - b) * (half - c))
        print('%s三角形的周长: ' % perimeter)
        print('%s三角形的面积: ' % area)
        break
    else:
        print('不能构成三角形, 请重新输入')
