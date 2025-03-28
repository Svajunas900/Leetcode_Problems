"""26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

"""Time complexity Big O(1)

Space complexity Big O(n)
"""

def removeDuplicates(nums: list) -> int:
    num = set(nums)
    print(num)
    return len(num)

    # With set
    # for i, x in enumerate(sorted(set(nums))):
    #     nums[i] = x
    # return len(sorted(set(nums)))
print(removeDuplicates([1,1,2]))
