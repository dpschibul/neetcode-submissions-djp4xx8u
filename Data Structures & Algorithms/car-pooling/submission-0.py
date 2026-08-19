class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # [4 passengers,from 1, to 2]

        start, end = min([f for p, f, t in trips]), max([t for p, f, t in trips])

        passengers = 0
        for i in range(start, end + 1):
            for p, f, t in trips:
                if t == i:
                    passengers -= p
                if f == i:
                    passengers += p
            if passengers > capacity:
                return False

        return True