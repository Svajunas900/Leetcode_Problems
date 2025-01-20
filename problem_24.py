"""24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""Time complexity Big O(n)

Space complexity Big O(1)
"""

def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    dummy = ListNode(0, head)
    prev, curr = dummy, head
    while curr and curr.next:
        next_pair = curr.next.next
        second = curr.next
        second.next = curr
        curr.next = next_pair
        prev.next = second
        prev = curr
        curr = next_pair
    return dummy.next
    