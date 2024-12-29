# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(list)
        q = deque([(root, 0)])
        level = 0
        while q:
            for _ in range(len(q)):
                node, col = q.popleft()
                if node:
                    mp[col].append((level, node.val))
                    q.append((node.left, col - 1))
                    q.append((node.right, col + 1))
            level += 1
        res = []
        for i in sorted(mp.keys()):
            mp[i].sort()
            res.append([val for _, val in mp[i]])
        return res
