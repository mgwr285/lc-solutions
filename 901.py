class StockSpanner:

    def __init__(self):
        self.day = 1
        self.stack = []

    def next(self, price: int) -> int:
        res = self.day
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        if self.stack:
            res = self.day - self.stack[-1][0]
        self.stack.append((self.day, price))
        self.day += 1
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
