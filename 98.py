# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(node):
            if not node:
                return True, float("inf"), -float("inf")
            lb, lmin, lmax = f(node.left)
            rb, rmin, rmax = f(node.right)
            return lb and rb and lmax < node.val < rmin, min(lmin, node.val), max(rmax, node.val)

        bal, _, _ = f(root)
        return bal
