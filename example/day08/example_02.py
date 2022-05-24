"""
example02 - 绘制爱心的代码

Author: Hx
Date: 2022/5/20
"""
from turtle import *

color('red')
begin_fill()
left(45)
forward(100)
circle(50, 180)
right(90)
circle(50, 180)
forward(100)
end_fill()
hideturtle()
