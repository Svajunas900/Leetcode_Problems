"""1926. Nearest Exit from Entrance in Maze


You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). 
You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] 
denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, 
and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. 
An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
"""


def nearest_exit(maze: list[list[str]], entrance: list[int]) -> int:
    m, n = len(maze), len(maze[0])
    x, y = entrance

    def is_exit(i, j): return i*j == 0 or i == m-1 or j == n-1

    def adj(i, j, dirs=[1, 0, -1, 0, 1]):
        for d in range(4):
            ii, jj = i + dirs[d], j + dirs[d+1]
            if 0 <= ii < m and 0 <= jj < n and maze[ii][jj] != "+":
                yield ii, jj

    dq = deque([(x, y, 0)])
    maze[x][y] = '+'
    while dq:
        i, j, s = dq.popleft()
        for ii, jj in adj(i, j):
            maze[ii][jj] = "+"
            if is_exit(ii, jj):
                return s+1
            dq.append((ii, jj, s+1))

    return -1
