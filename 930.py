class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        mp = defaultdict(int)
        l, s = 0, 0
        for r in range(len(nums)):
            s += nums[r]
            if s == goal:
                res += 1
            res += mp[s - goal]
            mp[s] += 1
        return res
