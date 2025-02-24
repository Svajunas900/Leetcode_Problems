"""2467. Most Profitable Path in a Tree

There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0. 
You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] 
indicates that there is an edge between nodes ai and bi in the tree.

At every node i, there is a gate. You are also given an array of even integers amount, where amount[i] represents:

the price needed to open the gate at node i, if amount[i] is negative, or,
the cash reward obtained on opening the gate at node i, otherwise.
The game goes on as follows:

Initially, Alice is at node 0 and Bob is at node bob.
At every second, Alice and Bob each move to an adjacent node. 
Alice moves towards some leaf node, while Bob moves towards node 0.
For every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
If the gate is already open, no price will be required, nor will there be any cash reward.
If Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. 
In other words, if the price to open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate is c, both of them receive c / 2 each.
If Alice reaches a leaf node, she stops moving. 
Similarly, if Bob reaches node 0, he stops moving. 
Note that these events are independent of each other.
Return the maximum net income Alice can have if she travels towards the optimal leaf node.
"""

def mostProfitablePath(edges: list[list[int]], bob: int, amount: list[int]) -> int:
  graph = {i: [] for i in range(len(amount))}
  for u, v in edges:
      graph[u].append(v)
      graph[v].append(u)
  
  bobPath = [-1] * len(amount)
  path = []

  def fillBobPath(node, parent):
      if node == 0:
          return True
      for neighbor in graph[node]:
          if neighbor != parent:
              path.append(node)
              if fillBobPath(neighbor, node):
                  return True
              path.pop()

  fillBobPath(bob, -1)
  for i, node in enumerate(path):
      bobPath[node] = i
  
  def getAliceMaxScore(node, parent, currScore, timestamp):
      if bobPath[node] == -1 or bobPath[node] > timestamp:
          currScore += amount[node]
      elif bobPath[node] == timestamp:
          currScore += amount[node] // 2
      return currScore if len(graph[node]) == 1 and node != 0 else max(getAliceMaxScore(neighbor, node, currScore, timestamp + 1) for neighbor in graph[node] if neighbor != parent)

  return getAliceMaxScore(0, -1, 0, 0)