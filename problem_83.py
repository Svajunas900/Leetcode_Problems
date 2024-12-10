"""83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.
"""

def deleteDuplicates(head):
    curr = head
    while curr and curr.next:
        print(curr.val)
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

