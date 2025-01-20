"""3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
"""

"""Time complexity Big O(n)
Function iterates through s length,
Therefore dominant term n 
built-in function max has complexity of O(1)
updating seen[currentChar], res, i is constant time operation O(1)
checking if current in seen is O(1) as well

Space complexity Big O(n)
i, j, res are scalar so the Big O(1) space
Due to the space used by the dictionary seen complexity of this
function is O(n)
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