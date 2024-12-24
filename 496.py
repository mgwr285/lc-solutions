class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = dict()
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                nge[nums2[stack.pop()]] = nums2[i]
            stack.append(i)
        res = []
        for num in nums1:
            res.append(nge.get(num, -1))
        return res
