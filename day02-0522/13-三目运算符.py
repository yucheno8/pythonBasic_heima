# -*-  codeing = utf-8 -*-
# @Time : 2021/5/22/022 23:21
# @Author : yucheno8
# @File ： 13-三目运算符.py
# @Software : PyCharm

# 三目运算符也叫三元运算符或三元表达式。

"""
# 语法：
    条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
"""
a = 1
b = 2
c = b if a > b else b
print(c)

# 需求：有两个变量，比较大小 如果变量1 大于 变量2 执行 变量1 - 变量2
aa = 10
bb = 6
cc = aa - bb if aa > bb else bb - aa
print(cc)
