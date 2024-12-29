# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def f(node, val):
            if node:
                if node.val < val:
                    node.right = f(node.right, val)
                elif node.val > val:
                    node.left = f(node.left, val)
                else:
                    if not node.left and not node.right:
                        return None
                    elif not node.left or not node.right:
                        return node.left if node.left else node.right
                    else:
                        t = node.left
                        while t.right:
                            t = t.right
                        node.val = t.val
                        node.left = f(node.left, t.val)
            return node

        return f(root, key)
