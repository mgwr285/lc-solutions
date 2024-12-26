class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k >= len(cardPoints):
            return sum(cardPoints)
        total, mn = 0, float("inf")
        l, s = 0, 0
        for r in range(len(cardPoints)):
            total += cardPoints[r]
            s += cardPoints[r]
            if r - l + 1 == len(cardPoints) - k:
                mn = min(mn, s)
                s -= cardPoints[l]
                l += 1
        return total - mn
