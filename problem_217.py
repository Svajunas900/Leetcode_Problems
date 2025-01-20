"""217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

"""Time complexity Big O(n)

Space complexity Big O(n)
"""

def containsDuplicate(self, nums: list) -> bool:
    dup = set()
    for i in nums:
        if i in dup:
            return True
        dup.add(i)
    return False

    # return sorted(list(set(nums))) != sorted(nums)