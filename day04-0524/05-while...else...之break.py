# -*-  codeing = utf-8 -*-
# @Time : 2021/5/24/024 20:28
# @Author : yucheno8
# @File ： 05-while...else...之break.py
# @Software : PyCharm

"""
所谓else指的是循环正常结束之后要执行的代码，即如果是break终止循环的情况，else下方缩进的代码将不执行。
"""

i = 1
while i <= 5:
    if i == 3:
        print('打印出错！')
        break
    print(f'{i}打印')
    i += 1
else:
    print('结束程序')
