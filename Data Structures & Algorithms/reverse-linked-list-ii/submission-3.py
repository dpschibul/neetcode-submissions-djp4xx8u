# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head

        start = 1
        prev = None
        while start < left:
            prev = cur
            cur = cur.next
            start += 1
        
        end = start
        cur2 = cur
        while end < right:
            cur2 = cur2.next
            end += 1
        
        endNode = None
        if cur2:
            endNode = cur2.next
            cur2.next = None


        def reverse(node: ListNode) -> list[ListNode]:
            prev = None
            cur = node
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            
            return [prev, node]


        revStart, revEnd = reverse(cur)

        if prev:
            prev.next = revStart
        
        revEnd.next = endNode

        if left > 1:
            return head
        else:
            return revStart
            


        

        

        