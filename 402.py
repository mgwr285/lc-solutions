class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while stack and c < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(c)
        while stack and k > 0:
            stack.pop()
            k -= 1
        res = "".join(stack).lstrip("0")
        return res if res else "0"
