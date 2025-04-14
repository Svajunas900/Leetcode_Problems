"""1534. Count Good Triplets

Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.


"""
def countGoodTriplets(arr: list[int], a: int, b: int, c: int) -> int:
  counter = 0
  length = len(arr)
  for i in range(length):
      for j in range(i+1, length):
          if abs(arr[i] - arr[j]) <= a:
              for k in range(j+1, length):
                  if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                      counter += 1    
  return counter