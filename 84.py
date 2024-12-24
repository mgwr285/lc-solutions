class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ps, ns = [-1] * len(heights), [len(heights)] * len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                ns[stack.pop()] = i
            if stack:
                ps[i] = stack[-1]
            stack.append(i)
        res = 0
        for i in range(len(heights)):
            h = heights[i]
            w = ns[i] - ps[i] - 1
            res = max(res, h * w)
        return res
