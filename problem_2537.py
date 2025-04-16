"""2537. Count the Number of Good Subarrays


Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.
"""


def countGood(nums: list[int], k: int) -> int:
    mpp = {}
    counter = left = 0
    for i in range(len(nums)):
        if nums[i] not in mpp:
            mpp[nums[i]] = 0
        k -= mpp[nums[i]]
        mpp[nums[i]] += 1
        while k <= 0:
            mpp[nums[left]] -= 1
            k += mpp[nums[left]]
            left += 1
        counter += left
    return counter


# var countGood = function(nums, k) {
#     let counter = 0;
#     let left = 0;
#     let hashMap = {};
#     for(let i = 0; nums.length > i; i++){
#         if(!(nums[i] in hashMap)){
#             hashMap[nums[i]] = 0
#         }
#         k -= hashMap[nums[i]]
#         hashMap[nums[i]] ++
#         while(k <= 0){
#             hashMap[nums[left]]--
#             k += hashMap[nums[left]]
#             left++
#         }
#         counter += left
#     }
#     return counter

# };
