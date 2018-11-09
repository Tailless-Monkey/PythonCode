#!/usr/bin/env python
# coding=utf-8
print(" ")
print(" ")
print("----欢迎使用最小公倍数计算器，下面请输入两个非零的正整数----")
print(" ")
print(" ")
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
if num1 == num2:
    print("最小公倍数是:%d" % num1)
elif num1%num2 == 0:
    print("最小公倍数是:%d" % num1)
elif num2%num1 == 0:
    print("最小公倍数是:%d" % num2)
elif num1 > num2:
    nn = num1*num2
    for i in range(2,nn):
        num3 = num1 * i % num2
        if num3 == 0:
            print(num1 * i)
            break
else:
    mm = num1*num2
    for x in range(2,mm):
        num3 = num2 * x % num1
        if num3 == 0:
            print(num2 * x)
            break

