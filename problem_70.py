def climbStairs(n: int) -> int:
    if n <= 3:
        return n
    
    prev1 = 3
    prev2 = 2
    cur = 0
    for _ in range(3, n):
        cur = prev1 + prev2
        prev2 = prev1
        prev1 = cur
    return cur


    # if cache is None:
    #         cache = {}
    #     if n in cache:
    #         return cache[n]
    #     if n == 0:
    #         return 1
    #     elif n == 1:
    #         return 1
    #     elif n == 2:
    #         return 2
    #     else:
    #         result = self.climbStairs(n - 1, cache) + self.climbStairs(n - 2, cache)
    #         cache[n] = result
    #         return result