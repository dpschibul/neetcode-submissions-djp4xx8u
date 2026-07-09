# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        visit = set()

        def dfs(node, level):
            if not node:
                return
            if level not in visit:
                res.append(node.val)
            
            visit.add(level)
            dfs(node.right, level+1)
            dfs(node.left, level+1)
        
        dfs(root, 0)

        return res
            

            
        