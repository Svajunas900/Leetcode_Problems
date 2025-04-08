"""2130. Maximum Twin Sum of a Linked List


In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
"""


def pairSum(self, head: Optional[ListNode]) -> int:
  slow = head
  fast = head
  res = 0
  i = 0
  arr = []
  while fast:
      arr.append(slow.val)
      i += 1
      slow = slow.next
      fast = fast.next.next
  i -= 1
  while slow:
      res = max(res, arr[i] + slow.val)
      slow = slow.next
      i -= 1
  return res