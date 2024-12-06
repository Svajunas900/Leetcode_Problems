def climbStairs(n) :
    if n <= 3:
        return n
    
    prev1 = 3
    prev2 = 2
    curr = 0
    for _ in range(3, n):
        cur = prev1 + prev2
        prev2 = prev1
        prev1 = cur
    return cur