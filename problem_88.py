"""88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

"""Time complexity Big O(m+n)

Space complexity Big O(1)
"""
def merge(nums1: list, m: int, nums2: list, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(m+n):
        if nums1[i] == 0 and i > m-1:
            nums1[i] = nums2[n-1]
            n -= 1
    nums1 = nums1.sort()