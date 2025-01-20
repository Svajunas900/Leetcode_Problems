"""1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""

"""Time complexity Big O(n)
The number of iterations is proportional to length of nums
To check if the target - n is in dictionary O(1)
Inserting new entry to dictionary O(1)
So the dominant term is the iteration through list O(n)

Space complexity O(n)
Using dictionary to store n elements, where n is the number of elements in the
input list nums
"""
def twoSum(nums: int, target:int) -> list: 
    a_dict = {}
    for i, n in enumerate(nums):
        if target - n in a_dict:
            return [i, a_dict[target - n]]
        a_dict[n] = i

    return 0
