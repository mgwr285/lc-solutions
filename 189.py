class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def f(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        k = k % len(nums)
        f(0, len(nums) - k - 1)
        f(len(nums) - k, len(nums) - 1)
        f(0, len(nums) - 1)
