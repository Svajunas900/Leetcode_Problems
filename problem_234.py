"""234. Palindrome Linked List

Given the head of a singly linked list, 
return true if it is a palindrome or false otherwise.
"""

"""Time complexity Big O(n)

Space complexity Big O(n)
"""

def isPalindrome(self, head) -> bool:
        self.curr = head
        return self.solve(head)
    
def solve(self, head):
    if head is None:
        return True
    ans = self.solve(head.next) and self.curr.val == head.val
    self.curr = self.curr.next
    return ans
