class Solution:
    def longestPrefix(self, s: str) -> str:
        MOD = 10 ** 9 + 7
        base = 29
        power = 1
        res, prefix, suffix = -1, 0, 0
        for i in range(len(s) - 1):
            prefix = ((prefix * base) % MOD + ord(s[i]) - ord("a") + 1) % MOD
            suffix = (((ord(s[len(s) - 1 - i]) - ord("a") + 1) * power) % MOD + suffix) % MOD
            if prefix == suffix:
                res = max(res, i)
            power = (power * base) % MOD
        return s[:res + 1]
