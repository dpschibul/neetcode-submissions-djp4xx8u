# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length+=1
        
        prev = None
        currPos = 0 
        curr = head
        starts = []
        ends = []

        while curr:
            if currPos == length - (length % k):
                ends.append(curr)
                break
            if currPos % k == 0:
                starts.append(curr)
                prev = None
            if currPos % k == k - 1:
                ends.append(curr)

            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
            currPos+=1
        
        for index in range(1, len(ends), 1):
            starts[index-1].next = ends[index]
        
        return ends[0]