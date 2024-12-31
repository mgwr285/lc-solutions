class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n = min(len(strs[0]), len(strs[-1]))
        i = 0
        while i < n and strs[0][i] == strs[-1][i]:
            i += 1
        return strs[0][:i]
