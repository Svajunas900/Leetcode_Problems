"""2342. Max Sum of a Pair With Equal Sum of Digits


You are given a 0-indexed array nums consisting of positive integers. 
You can choose two indices i and j, such that i != j, 
and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] 
that you can obtain over all possible indices i and j that satisfy the conditions.
"""

def maximumSum(nums: list[int]) -> int:
  mp = [-1] * 82  
  ans = -1

  for num in nums:
      digit_sum = sum(int(d) for d in str(num))

      if mp[digit_sum] != -1:
          ans = max(ans, num + mp[digit_sum])

      mp[digit_sum] = max(mp[digit_sum], num)

  return ans