# -*-  codeing = utf-8 -*-
# @Time : 2021/5/22/022 22:40
# @Author : yucheno8
# @File ： 10-if嵌套.py
# @Software : PyCharm

"""
if条件1：
    条件1成立执行的代码
    条件1成立执行的代码

    if条件2：
        条件2成立执行的代码
        条件2成立执行的代码

注意：条件2的if也是出于条件1的缩进关系内部。
"""

# 公交：如果有钱可以上车，没有钱，不能上车；如果上车了，判断是否能坐下 -- 是否有空座位

"""
1. 准备将来要做判断的数据：钱和空座
2. 判断是否有钱：上车和不能上本
3. 上车了：判断是否能坐下：有空座位 和 无空座位
"""
money = 1
seat = 0

if money == 1:
    print('土豪，请上车')
    if seat == 1:
        print('土豪，请坐')
    else:
        print('土豪，没有空座，站一站吧')
else:
    print('朋友，没带钱，跟着跑，跑快点')

