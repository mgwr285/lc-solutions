class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = defaultdict(int)
        for c in t:
            mp[c] += 1
        k = len(mp)
        start, length = -1, float("inf")
        l = 0
        for r in range(len(s)):
            mp[s[r]] -= 1
            if mp[s[r]] == 0:
                k -= 1
            while k == 0:
                if length > r - l + 1:
                    start = l
                    length = r - l + 1
                mp[s[l]] += 1
                if mp[s[l]] == 1:
                    k += 1
                l += 1
        if start == -1:
            return ""
        else:
            return s[start:start + length]
