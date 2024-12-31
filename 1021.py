class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        cnt = 0
        for c in s:
            if c == "(":
                cnt += 1
                if cnt == 1:
                    continue
                res.append(c)
            else:
                cnt -= 1
                if cnt == 0:
                    continue
                res.append(c)
        return "".join(res)
