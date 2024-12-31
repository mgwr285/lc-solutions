class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            l, r = k + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[k] == 0:
                    res.append([nums[l], nums[r], nums[k]])
                    while l < r and nums[l] + nums[r] + nums[k] == 0:
                        l += 1
                elif nums[l] + nums[r] + nums[k] < 0:
                    l += 1
                else:
                    r -= 1
        return res
