"""2206. Divide Array Into Equal Pairs

You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.
"""

def divideArray(nums: list[int]) -> bool:
    count_map = {}
    for num in nums:
        count_map[num] = count_map.get(num, 0) + 1
    
    for count in count_map.values():
        if count % 2 != 0:
            return False
    return True

divideArray([3,2,3,2,2,2])