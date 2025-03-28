"""735. Asteroid Collision


We are given an array asteroids of integers representing asteroids in a row. 
The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). 
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
"""

def asteroidCollision(asteroids: list[int]) -> list[int]:
  res = []
  for a in asteroids:
      while res and a < 0 < res[-1]:
          if -a > res[-1]:
              res.pop()
              continue
          elif -a == res[-1]:
              res.pop()
          break
      else:
          res.append(a)
  return res