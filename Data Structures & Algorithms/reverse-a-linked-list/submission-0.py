# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head

        else:
            prev = None
            p1 = head
            p2 = head

            while p2:
                p2 = p2.next
                p1.next = prev
                prev = p1
                p1 = p2

        return prev