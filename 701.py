# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def f(node):
            if not node:
                return TreeNode(val=val)
            if node.val <= val:
                node.right = f(node.right)
            else:
                node.left = f(node.left)
            return node

        return f(root)
