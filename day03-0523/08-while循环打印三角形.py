# -*-  codeing = utf-8 -*-
# @Time : 2021/5/24/024 9:07
# @Author : yucheno8
# @File ： 08-while循环打印三角形.py
# @Software : PyCharm
i = 0
while i < 5:
    j = 0
    while j <= i:
        print('*',end = '')
        j += 1
    print()
    i += 1