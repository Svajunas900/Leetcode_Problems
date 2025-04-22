"""547. Number of Provinces


There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 
if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""


def findCircleNum(isConnected: list[list[int]]) -> int:
    n = len(isConnected)
    visited = [False] * n
    count = 0

    def dfs(city):
        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                dfs(neighbor)

    for city in range(n):
        if not visited[city]:
            visited[city] = True
            dfs(city)
            count += 1
    return count
