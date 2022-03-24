"""
example_16 - 保存5个学生, 3门课程的成绩

Author: Hx
Date: 2022/3/24
"""
import random

names = ['井柏然', '杨紫', '李易峰', '王小二', '马云']
courses = ['语文', '数学', '英语']
# 列表的生成式语法
scores = [[random.randrange(50, 101) for _ in range(3)] for _ in range(len(names))]
print(scores)
for i, name in enumerate(names):
    for j, course in enumerate(courses):
        print('{0}的{1}成绩: {2}'.format(name, course, scores[i][j]))

# 统计每个学生的平均成绩
for i, name in enumerate(names):
    print('{0}的平均成绩: {1}'.format(name, sum(scores[i]) / len(courses)))

# 统计每门课程最高分和最低分
for j, course in enumerate(courses):
    temp = [scores[i][j] for i in range(len(names))]
    print('{0}的最高分: {1}'.format(course, max(temp)))
    print('{0}的最低分: {1}'.format(course, min(temp)))
