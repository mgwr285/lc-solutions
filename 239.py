class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        for i in range(len(nums)):
            if i >= k and nums[i - k] == queue[0]:
                queue.popleft()
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            if i >= k - 1:
                res.append(queue[0])
        return res
