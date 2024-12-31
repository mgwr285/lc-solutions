class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            tmp = [1] * (i + 1)
            for j in range(1, i):
                tmp[j] = res[-1][j - 1] + res[-1][j]
            res.append(tmp)
        return res
