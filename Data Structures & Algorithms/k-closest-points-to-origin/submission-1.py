class Solution:
    def euclidean_distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        priority = []
        for point in points:
            priority.append((self.euclidean_distance(point[0], point[1], 0, 0), point))
        heapq.heapify(priority)
        res = []

        for _ in range(k):
            res.append(heapq.heappop(priority)[1])

        return res