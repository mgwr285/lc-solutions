class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            ps, ns = [-1] * len(heights), [len(heights)] * len(heights)
            stack = []
            for i in range(len(heights)):
                while stack and heights[stack[-1]] > heights[i]:
                    ns[stack.pop()] = i
                if stack:
                    ps[i] = stack[-1]
                stack.append(i)
            for i in range(len(heights)):
                h = heights[i]
                w = ns[i] - ps[i] - 1
                res = max(res, h * w)
        return res
