class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight_map = defaultdict(list)

        for from_i, to_i, price_i in flights:
            flight_map[from_i].append((price_i, to_i))
        
        min_heap = []

        for price, dest in flight_map[src]:
            min_heap.append((price, dest, 0))
        
        heapq.heapify(min_heap)
        visited = {}

        while min_heap:
            price, dest, stops = heapq.heappop(min_heap)
            if stops > k:
                continue
            if dest == dst:
                return price
            visited = {}  
            if (dest, stops) in visited and visited[(dest, stops)] <= price:
                continue
            visited[(dest, stops)] = price

            for dp, d in flight_map[dest]:
                heapq.heappush(min_heap, (price + dp, d, stops + 1))
            
        return -1




