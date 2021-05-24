# -*-  codeing = utf-8 -*-
# @Time : 2021/5/24/024 20:22
# @Author : yucheno8
# @File ： 04-while...else.py
# @Software : PyCharm

# 循环可以和else配合使用，else下方缩进的代码指的是当循环正常结束之后要执行的代码'

"""
语法：
    while 条件:
        条件成立重复执行的代码
    else:
        循环正常结束之后要执行的代码
"""
i = 1
while i <= 5:
    print(f'{i}打印')
    i += 1
else:
    print('结束循环')