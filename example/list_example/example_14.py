"""
example_14 - 用一个列表保存54张扑克牌, 先洗牌
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
player_one = []
player_two = []
player_three = []

for _ in range(17):
    player_one.append(cards.pop())
    player_two.append(cards.pop())
    player_three.append(cards.pop())
player_one.sort(key=lambda x: x[2:])
player_two.sort(key=lambda x: x[2:])
player_three.sort(key=lambda x: x[2:])

player_one.extend(cards)
for one in player_one:
    print(one, end='\t')
print()
for two in player_two:
    print(two, end='\t')
print()
for three in player_three:
    print(three, end='\t')
