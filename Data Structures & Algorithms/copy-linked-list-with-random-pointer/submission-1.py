"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        copy_map = { None : None }

        while curr:
            copy_map[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            node = copy_map[curr]
            node.next = copy_map[curr.next]
            node.random = copy_map[curr.random]

            curr = curr.next
        
        return copy_map[head]