"""160. Intersection of Two Linked Lists

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

"""


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    a, b = headA, headB
    while (a != b):
        a = headB if not a else a.next
        b = headA if not b else b.next
    return a

