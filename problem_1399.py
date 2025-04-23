"""1399. Count Largest Group

You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.
"""


def countLargestGroup(self, n: int) -> int:
    hash_table = {}
    for i in range(1, n+1):
        res = self._helper(i)
        if res in hash_table:
            hash_table[res].append(i)
        else:
            hash_table[res] = [i]
    counter = 0
    max_group = 0
    for key, value in hash_table.items():
        length = len(value)
        if max_group < length:
            max_group = length
            counter = 1
        elif max_group == length:
            counter += 1

    return counter


def _helper(self, number):
    number_list = list(str(number))
    result = 0
    for i in number_list:
        result += int(i)
    return result
