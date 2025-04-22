"""841. Keys and Rooms


There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. 
Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. 
Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
return true if you can visit all the rooms, or false otherwise.
"""


def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    locked = [1]*len(rooms)
    queue = [0]
    head = 0
    while head < len(queue):
        if locked[queue[head]] == 0:
            head += 1
            continue
        locked[queue[head]] = 0
        for room in rooms[queue[head]]:
            if locked[room] == 1:
                queue.append(room)
        head += 1
    return sum(locked) == 0


canVisitAllRooms([[1], [2], [3], []])
