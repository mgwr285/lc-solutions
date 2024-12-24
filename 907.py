class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ps, ns = [-1] * len(arr), [len(arr)] * len(arr)
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                j = stack.pop()
                ns[j] = i
            if stack:
                ps[i] = stack[-1]
            stack.append(i)
        MOD = 10 ** 9 + 7
        res = 0
        for i in range(len(arr)):
            res = (res + ((arr[i] * (i - ps[i]) % MOD) * (ns[i] - i)) % MOD) % MOD
        return res
