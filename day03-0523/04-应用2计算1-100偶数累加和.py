# -*-  codeing = utf-8 -*-
# @Time : 2021/5/23/023 11:10
# @Author : yucheno8
# @File ： 04-应用2计算1-100偶数累加和.py
# @Software : PyCharm

# i = 1
# result = 0
# while i <= 100:
#     if i % 2 == 0:
#         result += i
#     i += 1
# print(f'1-100偶数累加和为{result}')

i = 0
result = 0
while i <= 100:
    result += i
    i += 2
print(f'1-100偶数累加和为{result}')

# while循环的注意事项：防止死循环
