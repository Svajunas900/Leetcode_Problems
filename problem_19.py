"""19. Remove Nth Node From End of List


Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head:
        return head
    dummy = ListNode(0, head)
    slow, fast = dummy, head
    for _ in range(n):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next