"""3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
"""

def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    i = 0
    res = 0

    for j in range(len(s)):
        currentChar = s[j]
        if currentChar in seen:
            i = max(i, seen[currentChar] + 1)
        seen[currentChar] = j
        res = max(res, j-i+1)
    
    return res