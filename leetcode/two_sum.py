'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

# First solution 2258ms runtime, 17.16mb memory
def two_sum(nums, target):
    length = len(nums)
    for index, value in enumerate(nums):
        compare_index = index + 1
        for i in range((length-1)-index):
            if nums[index] + nums[compare_index] == target:
                return [index, compare_index]
            else:
                compare_index += 1