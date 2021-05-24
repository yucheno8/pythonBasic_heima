# -*-  codeing = utf-8 -*-
# @Time : 2021/5/24/024 9:02
# @Author : yucheno8
# @File ： 07-while循环打印正方形.py
# @Software : PyCharm

i = 0
while i < 5:
    j = 0
    while j < 5:
        if(j == 4):
            print('*')
        else:
            print('*',end = '')
        j += 1
    i += 1