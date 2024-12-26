class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = [0] * 26
        l, res = 0, 0
        for r in range(len(s)):
            mp[ord(s[r]) - ord("A")] += 1
            while r - l + 1 - max(mp) > k:
                mp[ord(s[l]) - ord("A")] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
