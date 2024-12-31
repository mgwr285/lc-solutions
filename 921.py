class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res, cnt = 0, 0
        for c in s:
            if c == "(":
                cnt += 1
            else:
                if cnt == 0:
                    res += 1
                else:
                    cnt -= 1
        res += cnt
        return res
