#!/usr/bin/env python
# coding=utf-8

class Solution:
    def twoSum(self, nums, target): 
#使用循环的方式遍历列表中第一个元素和后一个元素的结果，直到找到符合条件的元素        
#        for i in range(0,len(nums)-1):
#            for j in range(i+1,len(nums)):
#                if nums[i] + nums[j] == target:
#                    return [i,j]
#将列表使用enumerate（）方法将其组合为索引序列，不去找两个数等于目标和，而是针对每个值，找出目标值和值的差值在不在这个列表中
        for i, num in enumerate(nums):
            sub_num = target - num
            if sub_num in nums:
                t_index =nums.index(sub_num)
                if t_index != i:
                    return [i, t_index]


nums = [x for x in range(0,100000)]
#将列表中的元素从大到小排列
#nums.sort(reverse = True)
target = int(input("please input a target number:"))
solution = Solution()
two_sum = solution.twoSum(nums,target)
print(two_sum)
