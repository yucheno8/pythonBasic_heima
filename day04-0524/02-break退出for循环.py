# -*-  codeing = utf-8 -*-
# @Time : 2021/5/24/024 20:17
# @Author : yucheno8
# @File ： 02-break退出for循环.py
# @Software : PyCharm

str1 = 'itheima'
for i in str1:
    # 当某些条件成立退出循环 -- break:条件 i取到字符e
    if i == 'e':
        break
    print(i,end='')