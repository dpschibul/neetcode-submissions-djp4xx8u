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

        res = []
        while q:
            length = len(q)
            cur = []
            for _ in range(length):
                node = q.popleft()

                cur.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if len(res) % 2 == 0:
                res.append(cur)
            else:
                res.append(cur[::-1])
        return res



        