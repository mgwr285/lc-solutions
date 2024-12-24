class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mins = [nums[0]]
        for i in range(1, len(nums)):
            mins.append(nums[i] if nums[i] < mins[i - 1] else mins[i - 1])
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack and mins[stack[-1]] < nums[i]:
                return True
            stack.append(i)
        return False
