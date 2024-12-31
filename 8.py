class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        res = 0
        s = s.strip()
        i, sign = 0, 1
        if i < len(s) and s[i] == "-":
            sign = -1
            i += 1
        elif i < len(s) and s[i] == "+":
            i += 1
        while i < len(s) and s[i].isdigit():
            if sign == 1 and (res > INT_MAX // 10 or res == INT_MAX // 10 and int(s[i]) > INT_MAX % 10):
                res = INT_MAX
                break
            elif sign == -1 and (res > -INT_MIN // 10 or res == -INT_MIN // 10 and int(s[i]) > -INT_MIN % 10):
                res = -INT_MIN
                break
            res = res * 10 + int(s[i])
            i += 1
        return sign * res
