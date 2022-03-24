"""
example_12 - 幸运的女人 (Josephu)
有15个男人和15个女人坐船出海了, 船坏了, 需要把其中15个人扔到海里, 其他人才能活下来;
所有人围成一圈, 有某个人从1开始依次报数, 报道9的人被扔到海里, 下一个人重新从1开始报数,
直到将15个人扔到海里, 最后, 15个女人都幸存了下来, 15个男人都被扔到了海里.
问原先哪些位置是男人, 哪些位置是女人

Author: Hx
Date: 2022/3/24
"""

persons = [True] * 30

index, counter, number = 0, 0, 0,
while counter < 15:
    if persons[index]:
        number += 1
        if number == 9:
            persons[index] = False
            counter += 1
            number = 0
    index += 1
    if index == 30:
        index = 0
print(persons)
for person in persons:
    print('女' if person else '男', end='\t')


