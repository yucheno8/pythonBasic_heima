# -*-  codeing = utf-8 -*-
# @Time : 2021/5/22/022 23:12
# @Author : yucheno8
# @File ： 12-应用：猜拳游戏（随机数）.py
# @Software : PyCharm
"""
步骤：
    1. 导入模块
    import random
    2. 使用这个模块中的功能
    random.randint(开始,结束)
"""
import random

# 1. 出拳
# 玩家
player = int(input('请出拳（0--石头；1--剪刀；2--布）:'))

# 电脑
computer = random.randint(0, 2)
print(f'电脑出拳为：{computer}')

# 2. 判断输赢
# 玩家获胜
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('玩家获胜，哈哈哈哈')
# 平局
elif ((player == 0) and (computer == 0)) or ((player == 1) and (computer == 1)) or ((player == 2) and (computer == 2)):
    print('平局')
# 电脑获胜
else:
    print('电脑获胜')
