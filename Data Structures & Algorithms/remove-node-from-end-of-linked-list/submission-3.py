# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        cur = head

        while cur:
            length+=1
            cur = cur.next
        
        cur_count = 0
        cur = head
        prev = None

        while cur:
            cur_count += 1
            if cur_count == length - n + 1:
                if prev == None:
                    return cur.next
                prev.next = cur.next
                return head
            prev = cur  
            cur = cur.next
        return head