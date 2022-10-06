"""
Two pointers is really an easy and effective technique that is typically used for searching pairs in a sorted array.

The algorithm basically uses the fact that the input array is sorted. We start the sum of extreme values (smallest and largest) and conditionally move both pointers. 
We move left pointer 'i' when the sum of A[i] and A[j] is less than X. We do not miss any pair because the sum is already smaller than X. Same logic applies for right 
pointer j.

Note : In order to apply 2 pointer technique, the list or array need to be sorted first.
"""

"""
Practice :

https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

class Solution:
    def twoSum(self, nums, target: int):
        nums_index = [[i,nums[i]] for i in range(0, len(nums))]
        nums_index.sort(key=lambda x: x[1]) #the default sort in python take O(nlogn)
        i = 0
        j = len(nums)-1
        while i < j: #This loop take O(n)
            if nums_index[i][1] + nums_index[j][1] < target:
                i+=1
            elif nums_index[i][1] + nums_index[j][1] > target:
                j-=1
            else:
                return [nums_index[i][0], nums_index[j][0]]
        # => overall the algorithm take : O(nlogn) + O(n) =  O(nlogn) < O(n^2)
        
        


