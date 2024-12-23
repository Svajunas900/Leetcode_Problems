"""206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""



def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return 
    previous = None
    curr = head
    ahead = head.next
    while ahead:
        curr.next = previous
        previous = curr
        curr = ahead
        ahead = ahead.next
    curr.next = previous
    return curr