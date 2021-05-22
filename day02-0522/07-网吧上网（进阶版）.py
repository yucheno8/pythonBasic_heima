# -*-  codeing = utf-8 -*-
# @Time : 2021/5/22/022 22:04
# @Author : yucheno8
# @File ： 07-网吧上网（进阶版）.py
# @Software : PyCharm

# 系统可以用户输入年龄，用这个年龄做条件判断
"""
1. 用户输入
2. 保存用户输入的年龄
3. if
***** 注意一个点：input接受到的数据是一个点，不能和18做判断 -- int转换类型
"""

age = int(input('请输入您的年龄：'))


if age >= 18:
    print(f'您输入的年龄是{age}，已经成年，可以上网。')

