"""
example_22 - 百钱百鸡问题 -
穷举法实现 : 穷尽所有的可能性, 然后设置条件, 找到问题的解--->也称暴力破解法

鸡翁一只5钱, 鸡母一只钱3, 小鸡三只钱1
Author: jet
Date: 2022/3/15
"""
# for x in range(0, 21):
#     for y in range(0, 34):
#         for z in range(0, 100, 3):
#             if x + y + z == 100 and 5 * x + 3 * y + z // 3 == 100:
#                 print(x, y, z)


for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if z % 3 == 0 and x + y + z == 100 and 5 * x + 3 * y + z // 3 == 100:
            print(x, y, z)
