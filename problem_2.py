"""2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""Time complexity Big O(max(n, m))
In the worst case scenario while loop will iterate through both linked lists n and m,
plus one because it can have carry leftover

Space complexity Big O(max(n, m))
On each iteration it creates node and appends it to result list.
Therefore complexity of the function is max(n, m) where n and m is the length of two linked lists
"""

def addTwoNumbers(l1: list, l2: list) -> None:
    dummy = ListNode()
    result = dummy
    total = carry = 0
    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        num = total % 10
        carry = total // 10
        result.next = ListNode(num)
        result = result.next
    return dummy.next