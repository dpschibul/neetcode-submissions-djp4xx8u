# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0

        while curr:
            curr = curr.next 
            count+=1

        toRemove = count - n

        currCount = 0

        curr = head
        prev = None
        while curr:
            if currCount == toRemove:
                if prev:
                    prev.next = curr.next
                else:
                    return curr.next
            prev = curr
            curr = curr.next
            currCount+=1 

        return head