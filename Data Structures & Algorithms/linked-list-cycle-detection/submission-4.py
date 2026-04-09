# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        node_set = set()

        while cur:
            if cur in node_set:
                return True
            node_set.add(cur)
            cur = cur.next
        return False
        