"""605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, 
flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""

def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
  for i in range(len(flowerbed)):
      if len(flowerbed) == 1 and flowerbed[i] == 0:
          flowerbed[i] = 1
          n -= 1
      if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
          flowerbed[i] = 1
          n -= 1
      if i == len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
          flowerbed[i] = 1
          n -= 1
      elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
          flowerbed[i] = 1
          n -= 1
      if n <= 0:
          return True
  return False
