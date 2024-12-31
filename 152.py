class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        mn, mx = nums[0], nums[0]
        for i in range(1, len(nums)):
            mn, mx = min(mn * nums[i], mx * nums[i], nums[i]), max(mn * nums[i], mx * nums[i], nums[i])
            res = max(res, mx)
        return res
