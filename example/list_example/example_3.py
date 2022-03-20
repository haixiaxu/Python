"""
example_3 - 输入10个整数, 计算平均值, 方差和标准差,找出最大值和最小值

Author: Haixia
Date: 2022/3/20
"""
nums = []
for _ in range(10):
    temp = int(input('请输入数据: '))
    nums.append(temp)
# 计算平均值
mean_value = sum(nums) / len(nums)
# 最大值
max_value = max(nums)
# 最小值
min_value = min(nums)

total = 0
for num in nums:
    total += (num - mean_value) ** 2
# 方差
var_value = total / (len(nums) - 1)
# 标准差
std_value = var_value ** 0.5
print('均值: {0}'.format(mean_value))
print('最大值: {0}'.format(max_value))
print('最小值: {0}'.format(min_value))
print('方差: {0}'.format(var_value))
print('标准差: {0}'.format(std_value))
print('极差: {0}'.format(max_value-min_value))


