"""1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""


def twoSum(nums: int, target:int) -> list:
    a_dict = {}
    for i, n in enumerate(nums):
        if target - n in a_dict:
            return [i, a_dict[target - n]]
        a_dict[n] = i

    return 0
