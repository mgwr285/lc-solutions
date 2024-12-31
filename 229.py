class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        e1, e2 = -float("nan"), -float("nan")
        c1, c2 = 0, 0
        for num in nums:
            if c1 == 0 and num != e2:
                e1, c1 = num, 1
            elif c2 == 0 and num != e1:
                e2, c2 = num, 1
            else:
                if num == e1:
                    c1 += 1
                elif num == e2:
                    c2 += 1
                else:
                    c1 -= 1
                    c2 -= 1
        c1, c2 = 0, 0
        for num in nums:
            if num == e1:
                c1 += 1
            elif num == e2:
                c2 += 1
        res = []
        if c1 > len(nums) // 3:
            res.append(e1)
        if c2 > len(nums) // 3:
            res.append(e2)
        return res
