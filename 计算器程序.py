#!/usr/bin/env python
# coding=utf-8
print('欢迎使用简易计算器,输入两个数字后会给出计算结果')
num1 = int(input('请输入第一个数:'))
num2 = int(input('请输入第二个数:'))
print('提供的算法如下:')
print('1、加法')
print('2、乘法')

select = int(input('请输入序号选择算法:'))
if select == 1:
    print(num1+num2)
else:
    print(num1*num2)
