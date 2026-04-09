# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0 
        maxPath = root.val
        
        def maxPathFunc(root):
            nonlocal maxPath
            if not root: return 0 

            leftMax = max(0, maxPathFunc(root.left))
            rightMax = max(0, maxPathFunc(root.right))
            maxPath = max(maxPath, root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        
        maxPathFunc(root)
        return maxPath


            
