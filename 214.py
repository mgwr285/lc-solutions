class Solution:
    def shortestPalindrome(self, s: str) -> str:
        MOD = 10 ** 9 + 7
        base = 29
        power = 1
        res, prefix, suffix = 0, 0, 0
        for i in range(len(s)):
            prefix = ((prefix * base) % MOD + ord(s[i]) - ord("a") + 1) % MOD
            suffix = (((ord(s[i]) - ord("a") + 1) * power) % MOD + suffix) % MOD
            if prefix == suffix:
                res = max(res, i)
            power = (power * base) % MOD
        suf = s[res + 1:]
        return suf[::-1] + s
