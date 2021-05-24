# -*-  codeing = utf-8 -*-
# @Time : 2021/5/24/024 8:34
# @Author : yucheno8
# @File ： 06-while嵌套循环.py
# @Software : PyCharm

"""
while嵌套语法：
    while 条件1:
        条件1成立执行的代码
        ......
        while 条件2:
            条件2成立执行的代码
            ......
总结：所谓while循环嵌套，就是一个while里面嵌套一个while的写法，每个while和之前的基础语法是相同的。
"""

"""
1. 循环打印3次
2. 今天刷晚饭的碗
3. 上面是一套惩罚，这一套惩罚要惩罚执行3天 -- 一套惩罚重复着执行 -- 放到一个while循环里面
"""

i = 0
while i < 3:
    j = 0
    while j < 3:
        print("媳妇，我错了")
        j += 1
    print('刷今天晚饭的碗。')
    i += 1


