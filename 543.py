# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def f(node):
            if not node:
                return 0, 0
            ld, ldepth = f(node.left)
            rd, rdepth = f(node.right)
            return max(ld, rd, ldepth + rdepth), 1 + max(ldepth, rdepth)

        d, _ = f(root)
        return d
