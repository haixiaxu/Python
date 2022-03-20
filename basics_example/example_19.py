"""
example_19 - 乘法口诀表

Author: jet
Date: 2022/3/15
"""

for i in range(1, 10):
    for j in range(1, i +1):
        print('{}x{}={}'.format(j,i,i*j), end='\t')
    print()