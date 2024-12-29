# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def f(node):
            if not node:
                return node
            if p.val <= node.val <= q.val:
                return node
            elif node.val <= p.val:
                return f(node.right)
            else:
                return f(node.left)
        if p.val > q.val:
            p, q = q, p
        return f(root)
