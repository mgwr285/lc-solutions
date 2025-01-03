# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def f(node, k):
            if not node:
                return node, k
            n, k = f(node.left, k)
            if n:
                return n, k
            k -= 1
            if k == 0:
                return node, k
            return f(node.right, k)

        node, k = f(root, k)
        return node.val
