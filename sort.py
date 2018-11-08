#!/usr/bin/env python
# coding=utf8

#定义一个查找并存储最小值的函数
def findSmallest(arr):
    smallest = arr[0]    #存储最小的值
    smallest_index = 0   #存储最小元素的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#定义一个排序的函数
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        #找出数组中最小的元素，并加入到新的数组中
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print (selectionSort([1,4,2,44,23,56,32,67,432,2345,322222,333,2214,32,3,23454]))

