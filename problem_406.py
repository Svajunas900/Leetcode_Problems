"""406. Queue Reconstruction by Height

You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). 
Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front 
who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. 
The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] 
is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).
"""

"""Time complexity Big O(n)

Space complexity Big O(n)
"""

def reconstructQueue(people: list) -> list:
  people = sorted(people, key=lambda x: (-x[0], x[1]))
  res = []
  for p in people:
      res.insert(p[1], p)
  return res

print(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))