"""35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

"""Time complexity Big O(log n)

Space complexity Big O(1)
"""
def searchInsert(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left

    # if target in nums:
    #     return nums.index(target)
    # else:
    #     nums.append(target)
    #     return sorted(nums).index(target)