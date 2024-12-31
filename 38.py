class Solution:
    def countAndSay(self, n: int) -> str:
        res = [1]
        for _ in range(n - 1):
            tmp = []
            i = 0
            while i < len(res):
                cnt = 0
                while i + cnt < len(res) and res[i + cnt] == res[i]:
                    cnt += 1
                tmp.extend([cnt, res[i]])
                i = i + cnt
            res = tmp
        return "".join([str(c) for c in res])
