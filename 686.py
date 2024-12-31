class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        res = 1
        tmp = a
        while len(a) < len(b):
            a += tmp
            res += 1
        if b in a:
            return res
        elif b in a + tmp:
            return res + 1
        return -1
