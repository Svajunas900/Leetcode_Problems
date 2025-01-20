"""11. Container With Most Water

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


"""Time complexity Big O(n)
n is the length of height list while loop moves pointer right
or left in each operation, so at most it will run n times

Space complexity Big O(1)
max_area, area, left and right has contant space O(1)
"""
def maxArea(height: list) -> int:
    max_area = 0
    left = 0
    right = len(height) - 1
    while left != right:
        if height[right] > height[left]:
            area = (right - left) * height[left]
            left += 1
        else:
            area = (right - left) * height[right] 
            right -= 1
        if max_area < area:
            max_area = area
    return max_area


print(maxArea([1,8,6,2,5,4,8,3,7]))