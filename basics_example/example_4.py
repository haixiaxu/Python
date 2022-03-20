"""
example_4 - 输入一个年份, 判断这个年份是不是闰年
规则: 四年一闰, 百年不闰, 四百年有闰
Author: jet
Date: 2022/3/13
"""

year = int(input('请输入年份'))

print(year % 4 == 0 and year % 100 == 0 and year % 400 == 0)