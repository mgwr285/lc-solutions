class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def f(k):
            res = 0
            mp = defaultdict(int)
            l = 0
            for r in range(len(nums)):
                mp[nums[r]] += 1
                while len(mp) > k:
                    mp[nums[l]] -= 1
                    if mp[nums[l]] == 0:
                        del mp[nums[l]]
                    l += 1
                res += r - l + 1
            return res

        return f(k) - f(k - 1)
