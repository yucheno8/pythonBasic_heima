# -*-  codeing = utf-8 -*-
# @Time : 2021/5/21/021 23:04
# @Author : yucheno8
# @File ： 07-格式化字符串.py
# @Software : PyCharm

name = 'TOM'
age = 18

# 我的名字是x，今年x岁了
print('我的名字是%s，今年%s岁了' % (name, age))

# 语法 f'{表达式}'
print(f'我的名字是{name}，今年{age}岁了')

# f-格式化字符串是Python3.6中新增的格式化方法，该方法更简单易读。z