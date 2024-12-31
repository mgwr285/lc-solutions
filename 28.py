class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        MOD = 10 ** 9 + 7
        base = 29
        power = pow(base, len(needle) - 1, MOD)
        hn, hh = 0, 0
        for c in needle:
            hn = ((hn * base) % MOD + (ord(c) - ord("a") + 1)) % MOD
        for i in range(len(haystack)):
            if i >= len(needle):
                hh = (hh - (ord(haystack[i - len(needle)]) - ord("a") + 1) * power % MOD) % MOD
            hh = ((hh * base) % MOD + (ord(haystack[i]) - ord("a") + 1)) % MOD
            if i >= len(needle) - 1 and hn == hh:
                start = i - len(needle) + 1
                if haystack[start:start + len(needle)] == needle:
                    return start
        return -1
