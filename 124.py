# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def f(node):
            if not node:
                return 0, -float("inf")
            ld, lsum = f(node.left)
            rd, rsum = f(node.right)
            return max(max(ld, rd) + node.val, node.val), max(lsum, rsum, ld + node.val, ld + node.val + rd, node.val, node.val + rd)

        _, s = f(root)
        return s
