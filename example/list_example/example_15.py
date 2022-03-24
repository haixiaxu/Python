"""
example_15 - 用一个列表保存54张扑克牌, 先洗牌
再按斗地主的发牌方式把牌发给三个玩家, 多的3张牌给第一个玩家(地主)
最后把每个玩家手上的牌显示出来

Author: Hx
Date: 2022/3/24
"""
import random

suites = ['♠', '♥', '♣', '♦']
faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cards = []
for suite in suites:
    for face in faces:
        cards.append('{0}{1}'.format(suite, face))
cards.append('小王')
cards.append('大王')
# 随机乱序, 进行洗牌
random.shuffle(cards)

# 嵌套列表 (列表中的元素又是列表)
players = [[] for _ in range(3)]

for _ in range(17):
    for player in players:
        # 删除元素 (默认删除最后一个元素)
        player.append(cards.pop())
# 将一个列表的元素合并到另一个列表中
players[0].extend(cards)
for player in players:
    # sort 对列表中的元素进行排序
    player.sort(key=lambda x: x[1:])
    for card in player:
        print(card, end=' ')
    print()
