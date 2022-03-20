"""
example_23 - 
5个人(abcde)晚上去捕鱼,捕了不计其数的鱼, 然后累了去睡觉.
第二天, a第一个醒来, 把鱼分成了5份, 扔掉多余的1条, 然后拿走了自己的1份;
b第二个醒来, 以为鱼没有分过, 把剩下的鱼分成了5份, 扔掉多余的1条, 拿走了自己的1份
c, d, e依次醒过来, 都按照同样的方法来分鱼.

Author: jet
Date: 2022/3/17
"""
# 假设总共有6条鱼
fish = 1
while True:
    # 假设鱼够分
    is_mark = True
    total = fish
    for i in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            is_mark = False
    # 假设鱼够分, 输出鱼的数量, 并且输出数量并退出循环
    if is_mark:
        print(fish)
        break
    # 如果不够分, 就继续累加
    fish += 1
