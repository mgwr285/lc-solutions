# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def f(p, q):
            if not p and not q:
                return True
            elif p and q:
                return p.val == q.val and f(p.left, q.right) and f(p.right, q.left)
            else:
                return False

        if not root:
            return True
        else:
            return f(root.left, root.right)
