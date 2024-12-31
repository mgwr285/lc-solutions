class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for r in range(len(nums)):
            if l - 1 >= 0 and nums[l - 1] == nums[r]:
                continue
            nums[l] = nums[r]
            l += 1
        return l
