class Solution:
    def maxDepth(self, s: str) -> int:
        curr_max, g_max = 0, 0
        for c in s:
            if c == "(":
                curr_max += 1
                g_max = max(g_max, curr_max)
            elif c == ")":
                curr_max -= 1
        return g_max
