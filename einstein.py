#!/usr/bin/env python
# coding=utf-8
##说明：爱因斯坦曾出过这样一道有趣的数学题:有一个长阶梯，若每步上2 阶，最后剩1 阶; 若每步上 3 阶，最后剩 2 阶;若每步上 5 阶，最后剩 4 阶;若每步上 6 阶，最后剩 5 阶;只有每步上 7 阶，最后刚好一阶也不剩。
x = 7
i = 1 
flag = 0
while i <= 100:
    if ( i % 2 == 1 ) and ( x % 3 == 2 ) and ( x % 5 == 4 ) and ( x % 6==5 ):
        flag = 1 
    else:
# 根据题意，x 一定是 7 的整数倍，所以每次乘以 7 i+=1
        x = 7 * (i+1)
    i +=1
if flag == 1: 
    print('阶梯数是:', x)
else: 
    print('在程序限定的范围内找不到答案!')
