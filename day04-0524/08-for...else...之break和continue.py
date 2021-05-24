# -*-  codeing = utf-8 -*-
# @Time : 2021/5/24/024 20:36
# @Author : yucheno8
# @File ： 08-for...else...之break和continue.py
# @Software : PyCharm

str1 = 'itheima'
for i in str1:
    if i == 'e':
        print('打印出错')
        break
    print(f'{i}打印')
else:
    print('程序结束。')

# 因为continue是退出当前一次循环，继续下一次循环，所以该循环在continue控制下是可以正常结束的，当循环结束后，则执行了else缩进的代码。

# str1 = 'itheima'
# for i in str1:
#     if i == 'e':
#         print('打印出错')
#         continue
#     print(f'{i}打印')
# else:
#     print('程序结束。')