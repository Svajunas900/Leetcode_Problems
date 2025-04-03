"""2095. Delete the Middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, 
where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
"""
def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
  if head.next is None:
      return None
  prev = ListNode(None, next=head)
  pointer = head
  fast_pointer = head
  while fast_pointer and fast_pointer.next:
      prev = prev.next
      pointer = pointer.next
      fast_pointer = fast_pointer.next.next
  prev.next = pointer.next
  return head