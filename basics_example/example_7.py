"""
example_7 - 英制单位转公制单位 (英寸--->厘米)
Author: jet
Date: 2022/3/13
"""
x = float(input(('请输入长度(英寸):')))
print('%s 英寸=%s厘米' % (x, 2.54 * x))
import getpass

username = input('用户名:')
password = input('密码:')

if username == 'admin' and password == '123':
    print('欢迎登录***系统')
else:
    print('用户名或密码错误')
print('程序结束, 再见!!')