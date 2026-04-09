# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def traverseAndInsert(node: Optional[TreeNode]) -> None:
            if not node:
                return
            if node.val < val:
                if node.right:
                    traverseAndInsert(node.right)
                else:
                    node.right = TreeNode(val)
            else:
                if node.left:
                    traverseAndInsert(node.left)
                else:
                    node.left = TreeNode(val)
        traverseAndInsert(root)
        return root
        