# -*-  codeing = utf-8 -*-
# @Time : 2021/5/22/022 19:46
# @Author : yucheno8
# @File ： 02-转换数据类型.py
# @Software : PyCharm
"""
转换数据类型的函数：
int(x[,base])         -- 将x转换为一个整数
float(x)              -- 将x转换为一个浮点数
complex(real[,imag])  -- 创建一个复数，real为实部，imag为虚部
str(x)                -- 将对象x转换为字符串
repr(x)               -- 将对象x转换为表达式字符串
eval(str)             -- 用来计算在字符串中的有效Python表达式，并返回一个对象
tuple(s)              -- 将序列s转换为一个元组
list(s)               -- 将序列s转换为一个列表
chr(x)                -- 将一个整数转换为一个Unicode字符
ord(x)                -- 将一个字符转换为它的ASCII整数值
hex(x)                -- 将一个整数转换为一个十六进制字符串
oct(x)                -- 将一个整数转换为一个八进制字符串
bin(x)                -- 将一个整数转换为一个二进制字符串
"""

"""
1. input

2. 检测input数据类型str

3. int() 转换数据类型

4. 检测是否转换成功
"""
num = input('请输入数字：')
print(num)
print(type(num)) # str

print(type(int(num))) # int

