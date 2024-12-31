class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def f(l, r):
            if l >= r:
                return
            nonlocal res
            mid = l + (r - l) // 2
            f(l, mid)
            f(mid + 1, r)
            j = mid + 1
            for i in range(l, mid + 1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                res += j - (mid + 1)
            i, j = l, mid + 1
            tmp = []
            while i <= mid or j <= r:
                if i <= mid and j <= r:
                    if nums[i] <= nums[j]:
                        tmp.append(nums[i])
                        i += 1
                    else:
                        tmp.append(nums[j])
                        j += 1
                elif i <= mid:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1
            nums[l:r + 1] = tmp[:]

        res = 0
        f(0, len(nums) - 1)
        return res
