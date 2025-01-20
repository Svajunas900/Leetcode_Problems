"""5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
"""

"""Time complexity Big O(n^2)
Outer loop runs 0 to len(s)-1 iterating through each character in the string
Therefore this results in Big O(n)
Helper function expand_around_center is called twice and it 
checks both odd and even-length palindromes. 
In worst case scenario expand_around_center function could expand
up to the entire length of the string. So overall time complexity
O(n^2)


Space complexity Big O(n)
start, end, odd, even, max_length are not dependent on the input
so the it has constant space complexity O(1)
The space required to store final string depends on the s input so the
space complexity is O(n)
"""
def longestPalindrome(s: str) -> str:
    if len(s) == 0:
        return s
    
    def expand_around_center(s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    start = 0
    end = 0

    for i in range(len(s)):
        odd = expand_around_center(s, i, i)
        even = expand_around_center(s, i, i+1)
        max_length = max(odd, even)
        
        if max_length > end - start:
            start = i - (max_length - 1) // 2
            end = i + max_length // 2

    return s[start:end+1] 