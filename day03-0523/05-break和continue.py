# -*-  codeing = utf-8 -*-
# @Time : 2021/5/23/023 11:22
# @Author : yucheno8
# @File ： 05-break和continue.py
# @Software : PyCharm

# break和continue是循环中满足一定条件退出循环的两种不同方式。

# 情况一：break -- 当某些条件成立，退出整个循环
# i = 1
# while i <= 5:
#     if i == 4:
#         print(f'吃饱了，不吃了')
#         break
#     print(f'吃了第{i}个苹果')
#     i += 1

# 情况二：continue -- 当某些条件成立，退出当前循环，进行下一次循环
i = 1
while i <= 5:
    if i == 3:
        print(f'这是我要吃的第{i}个苹果，它是坏的，我不吃了，我要吃下一个苹果了')
        # 如果使用continue，在continue前一定哟啊修改计数器，否则进入死循环
        i += 1
        continue
    print(f'我吃了第{i}个苹果')
    i += 1