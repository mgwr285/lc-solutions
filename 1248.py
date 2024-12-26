class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        mp = defaultdict(int)
        l, s = 0, 0
        for r in range(len(nums)):
            s += nums[r] % 2
            if s == k:
                res += 1
            res += mp[s - k]
            mp[s] += 1
        return res
