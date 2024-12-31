class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for num in nums:
            if num - 1 in nums:
                continue
            l = 0
            while num + l in nums:
                l += 1
            res = max(res, l)
        return res
