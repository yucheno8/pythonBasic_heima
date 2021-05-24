# -*-  codeing = utf-8 -*-
# @Time : 2021/5/24/024 9:12
# @Author : yucheno8
# @File ： 09-while循环打印九九乘法表.py
# @Software : PyCharm
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i}*{j}={i*j}',end='\t')
        i += 1
    print()
    j += 1