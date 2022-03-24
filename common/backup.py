# -*- coding: utf-8 -*-

"""
backup - 压缩备份文件

Author: Hx
Date: 2022/3/24
"""
import os
import time

# 将要备份的文件和目录分配到一个列表中
source = ['"D:\\pcap"']

# 必须备份到主目录中
target_dir = 'D:\\Testing'

if not os.path.exists(target_dir):
    # 创建文件夹
    os.mkdir(target_dir)
    print('创建文件成功', target_dir)

# 文件需要备份到 zip 里, 当前日期是子目录的名称
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 当前时间是 zip 存档的名称
now = time.strftime('%H%M%S')
target = today + os.sep + now + '.zip'
# 如果目录不存在则创建
if not os.path.exists(today):
    # 创建文件夹
    os.mkdir(today)
    print('创建文件成功', today)

# 使用 zip 命令把文件放到 zip 存档里
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# 运行备份程序
print('Zip command is: ')
print(zip_command)
print('成功: ' + target if os.system(zip_command) == 0 else '失败')
