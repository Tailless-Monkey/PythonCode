#!/usr/bin/env python
# coding=utf-8
#说明：输入一个数，自动计算出这个数下面的所有奇数
i = int(input("请输入一个正整数："))
while i:
    if i % 2 == 0:
        i -= 1
        print(i)
    else:
        i -= 1
