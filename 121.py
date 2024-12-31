class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = prices[0]
        for i in range(1, len(prices)):
            if l < prices[i]:
                res = max(res, prices[i] - l)
            else:
                l = prices[i]
        return res
