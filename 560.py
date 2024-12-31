class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        mp, s = defaultdict(int), 0
        for i in range(len(nums)):
            s += nums[i]
            if s == k:
                res += 1
            if s - k in mp:
                res += mp[s - k]
            mp[s] += 1
        return res
