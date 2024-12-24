class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        l, cnt, res = 0, 0, 0
        for r in range(len(s)):
            mp[s[r]] += 1
            if mp[s[r]] > 1:
                cnt += 1
            while cnt > 0:
                mp[s[l]] -= 1
                if mp[s[l]] == 1:
                    cnt -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
