"""1732. Find the Highest Altitude


There is a biker going on a road trip. 
The road trip consists of n + 1 points at different altitudes. 
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). 
Return the highest altitude of a point.
"""


def largestAltitude(gain: list[int]) -> int:
  for i in range(1, len(gain)):
      gain[i] += gain[i-1]
  max_alt = max(gain)
  if max_alt < 0:
      return 0
  return max_alt