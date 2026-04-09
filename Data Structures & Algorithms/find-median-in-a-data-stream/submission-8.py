class MedianFinder:

    def __init__(self):
        # lower half of the inserted elements
        self.lower = []
        # upper half of the inserted elements
        self.upper = []
        

    def addNum(self, num: int) -> None:
        if not self.lower:
            heapq.heappush(self.lower, -num)
            return 
        if num > abs(self.lower[0]):
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -num)

        if len(self.lower) > len(self.upper) + 1:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        if len(self.upper) > len(self.lower) + 1:
            heapq.heappush(self.lower, -heapq.heappop(self.upper))
        

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        elif len(self.upper) > len(self.lower):
            return self.upper[0]
           
        left_max, right_min = -self.lower[0], self.upper[0]

        return ((left_max + right_min) / 2)


        
        