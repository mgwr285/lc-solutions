class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        for i in range(len(nums) * 2):
            while stack and nums[stack[-1] % len(nums)] < nums[i % len(nums)]:
                res[stack.pop() % len(nums)] = nums[i % len(nums)]
            stack.append(i)
        return res
