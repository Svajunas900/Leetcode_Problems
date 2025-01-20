"""1346. Check If N and Its Double Exist

Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]"""

"""Time complexity Big O(n)

Space complexity Big O(n)
"""

def checkIfExist(arr: list) -> bool:
    a_dict = {}
    for index, value in enumerate(arr):
        if value * 2 in a_dict and a_dict[value * 2] != index:
            return True
        elif value / 2 in a_dict and a_dict[value / 2] != index:
            return True
        else:
            a_dict[value] = index
    return False
