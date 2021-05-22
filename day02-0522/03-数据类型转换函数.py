# -*-  codeing = utf-8 -*-
# @Time : 2021/5/22/022 20:03
# @Author : yucheno8
# @File ： 03-数据类型转换函数.py
# @Software : PyCharm
#1. float() -- 将数据转换成浮点型
num1 = 1
str1 = '10'
print(float(num1))
print(float(str1))

# 2. str() -- 将数据转换成字符串型
print(str(num1))

# 3. tuple() -- 将一个序列转换成元组
list1 = [10, 20, 30]
print(tuple(list1))

# 4. list() -- 将一个序列转换成列表
t1 =(100, 200, 300)
print(list(t1))

# 5. eval() -- 计算字符串中的有效Python表达式，并返回一个对象
str2 = '1'
str3 = '1.1'
str4 = '(1000, 2000,3000)'
str5 = '[1000, 2000, 3000]'
print(eval(str2))
print(eval(str3))
print(eval(str4))
print(eval(str5))

