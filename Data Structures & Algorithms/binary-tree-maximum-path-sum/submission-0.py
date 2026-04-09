# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def getMaximum(node):
            if not node:
                return 0
            
            leftMax = getMaximum(node.left)
            rightMax = getMaximum(node.right)
            pathSum = node.val + max(0, leftMax) + max(0, rightMax)
            res[0] = max(pathSum, res[0])

            return node.val + max(0, max(leftMax, rightMax))
        
        getMaximum(root)
        return res[0]
