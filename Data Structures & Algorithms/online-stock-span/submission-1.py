class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        total_span = 1
        while self.stack and self.stack[-1][0] <= price:
            _, span = self.stack.pop()
            total_span += span
        self.stack.append([price, total_span])
        return total_span

        

# [100], [80], [60], [70], [60], [75], [85]

# [100] = 1
# [80] = 1
# [60] = 1
# [60, 70] = 2
# [60, 70, 75] = 3
# []

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)