class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        last, res = float("inf"), 0
        for c in s:
            val = mp[c]
            res += val
            if val > last:
                res -= 2 * last
            last = val
        return res
