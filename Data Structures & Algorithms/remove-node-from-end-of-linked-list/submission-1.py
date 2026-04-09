# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = r = head
        count = 0 
        prev = None
        while r:
            if count == n:
                prev = l
                l = l.next
            else:
                count+=1
            r = r.next
        if prev:
            prev.next = l.next
        else:
            return l.next
        
        return head
