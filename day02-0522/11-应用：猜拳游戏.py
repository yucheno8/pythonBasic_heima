# -*-  codeing = utf-8 -*-
# @Time : 2021/5/22/022 22:51
# @Author : yucheno8
# @File ： 11-应用：猜拳游戏.py
# @Software : PyCharm
"""
1. 出拳
    玩家：手动输入
    电脑：1. 固定：剪刀；2. 随机
2. 判断输赢
    2.1 玩家获胜
    2.2 平局
    2.3 电脑获胜
"""

# 1. 出拳
# 玩家
player = int(input('请出拳：0--石头；1--剪刀；2--布'))
# 电脑
computer = 1

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