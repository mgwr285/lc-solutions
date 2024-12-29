# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def f(node):
            if not node:
                return True, 0
            lbal, ldepth = f(node.left)
            rbal, rdepth = f(node.right)
            return lbal and rbal and abs(ldepth - rdepth) <= 1, 1 + max(ldepth, rdepth)

        bal, _ = f(root)
        return bal
