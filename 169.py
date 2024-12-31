class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        e, cnt = nums[0], 1
        for i in range(1, len(nums)):
            if cnt == 0:
                e, cnt = nums[i], 1
            else:
                if nums[i] == e:
                    cnt += 1
                else:
                    cnt -= 1
        return e
