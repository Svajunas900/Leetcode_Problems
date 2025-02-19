"""14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""


"""Time complexity Big O(m log m)

sorting the list of string takes (m⋅log(k))
m is the average length of the strings in the list
k is the number of string in the list

Space complexity Big O(m)
the space complexity of sorting is O(m) in the worst case.
"""

def longestCommonPrefix(strs: list) -> str:
    result = ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    if len(strs) == 1:
        return strs[0]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return result
        result += first[i]
    return result