# -*-  codeing = utf-8 -*-
# @Time : 2021/5/22/022 22:12
# @Author : yucheno8
# @File ： 08-if...else...语句.py
# @Software : PyCharm
"""
if条件：
    条件成立执行的代码1
    条件成立执行的代码2
else：
    条件不成立执行的代码1
    条件不成立执行的代码2
"""

age = int(input('请输入您的年龄：'))

if age >= 18:
    print(f'您输入的年龄是{age}，已经成年，可以上网。')
else:
    print(f'您输入的年龄是{age}，小朋友，回家写作业去')
