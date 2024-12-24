class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ps, ns = [-1] * len(nums), [len(nums)] * len(nums)
        pg, ng = [-1] * len(nums), [len(nums)] * len(nums)
        stack1, stack2 = [], []
        for i in range(len(nums)):
            while stack1 and nums[stack1[-1]] > nums[i]:
                j = stack1.pop()
                ns[j] = i
            if stack1:
                ps[i] = stack1[-1]
            stack1.append(i)

            while stack2 and nums[stack2[-1]] < nums[i]:
                j = stack2.pop()
                ng[j] = i
            if stack2:
                pg[i] = stack2[-1]
            stack2.append(i)
        res = 0
        for i in range(len(nums)):
            res += nums[i] * ((i - pg[i]) * (ng[i] - i) - (i - ps[i]) * (ns[i] - i))
        return res
