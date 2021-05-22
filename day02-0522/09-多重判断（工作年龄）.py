# -*-  codeing = utf-8 -*-
# @Time : 2021/5/22/022 22:22
# @Author : yucheno8
# @File ： 09-多重判断（工作年龄）.py
# @Software : PyCharm

"""
需求：
    如果年龄小于18，为童工，不合法
    如果年龄18-60岁之间，为合法工作年龄
    如果年龄大于60为退休年龄
"""

age = int(input('请输入您的年龄：'))

# if age < 18:
#     print(f'您输入的年龄是{age}，为童工，不合法。')
# elif age < 60:
#     print(f'您输入的年龄是{age}，为合法工作年龄。')
# else:
#     print(f'您输入的年龄是{age}，为退休年龄。')

# 童工
if age < 18:
    print(f'您输入的年龄是{age}，童工')

# 18-60合法
elif (age >= 18) and (age <= 60): # 拓展：age >= 18 and age <= 60 可以化简为 18 <= age <= 60
    print(f'您输入的年龄是{age}，合法')

# 大于60退休
elif age > 60:
    print(f'您输入的年龄是{age}，退休年龄')



