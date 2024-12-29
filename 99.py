# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def f(curr):
            if not curr:
                return
            nonlocal prev, p, q
            f(curr.left)
            if not p and prev.val >= curr.val:
                p = prev
            if p and prev.val >= curr.val:
                q = curr
            prev = curr
            f(curr.right)

        prev = TreeNode(val=-float("inf"))
        p, q = None, None
        f(root)
        if p and q:
            p.val, q.val = q.val, p.val
        return root
