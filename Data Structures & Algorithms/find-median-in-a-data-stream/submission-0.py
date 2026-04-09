class MedianFinder:

    def __init__(self):
        self.data = []
        

    def addNum(self, num: int) -> None:
        self.data.append(num)

        

    def findMedian(self) -> float:
        if not self.data:
            return []
        self.data.sort()
        mid = len(self.data) // 2

        return self.data[mid] if len(self.data) % 2 != 0 else ((self.data[mid] + self.data[mid-1]) / 2
)
        
        