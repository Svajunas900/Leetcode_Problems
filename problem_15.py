"""15. 3Sum

Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


def threeSum(nums):
    result = []
    nums = sorted(nums)
    previous = None
    for num in range(len(nums)-1):
        if previous == nums[num]:
            continue
        left = num+1
        right = len(nums)-1
        previous = nums[num]
        while left != right:
            three = nums[num] + nums[left] + nums[right]
            if three == 0:
                result.append([nums[num], nums[left], nums[right]])
            if three > 0:
                right -= 1
            else: 
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
    return result

print(threeSum([0,0,0,0]))