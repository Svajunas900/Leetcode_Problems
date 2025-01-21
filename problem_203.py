"""203. Remove Linked List Elements

Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



def removeElements(head: Optional[ListNode], val:int) -> Optional[ListNode]:
    if not head:
        return 
    previous = ListNode(0, head)
    curr = previous
    while curr:
        while curr.next and curr.next.val == val:
            curr.next = curr.next.next
        curr = curr.next  
    return previous.next