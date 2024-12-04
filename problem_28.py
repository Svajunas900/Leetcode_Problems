"""28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
"""


def strStr(haystack, needle):
    left = 0 
    right = len(needle)
    for i in range(len(haystack)):
        if haystack[left:right] == needle:
            return i
        else:
            left += 1
            right += 1
        if right > len(haystack):
            return -1