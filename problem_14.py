"""14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""


def longestCommonPrefix(strs):
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