"""1079. Letter Tile Possibilities


You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
"""

def numTilePossibilities(tiles: str) -> int:
        tiles = sorted(tiles)
        used = [False] * len(tiles)
        return backtrack(tiles, used)


def backtrack(tiles, used):
    count = 0
    for i in range(len(tiles)):
        if used[i] or (i > 0 and tiles[i] == tiles[i - 1] and not used[i-1]):
            continue
        used[i] = True
        count += 1 + backtrack(tiles, used)
        used[i] = False
    return count


print(numTilePossibilities("AAB"))