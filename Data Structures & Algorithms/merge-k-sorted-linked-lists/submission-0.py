# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range (0, len(lists), 2):
                if i+1 < len(lists):
                    mergedLists.append(self.mergeList(lists[i], lists[i+1]))
                else:
                    mergedLists.append(lists[i])


            lists = mergedLists

        return lists[0]

    def mergeList(self, a, b):
        dummy = ListNode(0)
        curr = dummy

        while a and b:
            if a.val < b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            curr = curr.next

            curr.next = a or b 
        return dummy.next
                