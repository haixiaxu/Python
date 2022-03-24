"""
example_13 - 

Author: Hx
Date: 2022/3/24
"""
persons = [i for i in range(1, 31)]

for _ in range(15):
    persons = persons[9:] + persons[:8]
print(persons)
for i in range(1, 31):
    print('女' if i in persons else '男', end='\t')
