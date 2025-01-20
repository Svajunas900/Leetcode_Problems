"""16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""

"""Time complexity Big O(n^2)

Space complexity Big O(n)
"""
def threeSumClosest(nums: list, target: int) -> int:
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2):
        left, right = i + 1, len(nums) - 1
        while left != right:
            three_sum = nums[i] + nums[left] + nums[right]
            if abs(closest - target) > abs(three_sum - target):
                closest = three_sum
            if three_sum == target: return target
            if three_sum > target:
                right -= 1
            else:
                left += 1
    return closest

print(threeSumClosest([-1,2,1,-4], 1))