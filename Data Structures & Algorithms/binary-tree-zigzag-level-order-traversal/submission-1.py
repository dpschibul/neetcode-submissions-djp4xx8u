# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])

        level = 0
        res = []

        while q:
            size = len(q)
            cur = []

            for i in range(size):
                node = q.popleft()

                cur.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left: 
                    q.append(node.left)
            if level % 2 == 1:
                res.append(cur)
            else:
                res.append(cur[::-1])
            level += 1
        
        return res




        
        