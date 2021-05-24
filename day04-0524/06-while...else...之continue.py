# -*-  codeing = utf-8 -*-
# @Time : 2021/5/24/024 20:31
# @Author : yucheno8
# @File ： 06-while...else...之continue.py
# @Software : PyCharm


"""
因为continue是退出当前一次循环，继续下一次循环，所以该循环在continue控制下是可以正常结束的，当循环结束后，则执行了else缩进的代码。
"""
i = 1
while i <= 5:
    if i == 3:
        print('打印出错！')
        i += 1
        continue
    print(f'{i}打印')
    i += 1
else:
    print('结束程序')