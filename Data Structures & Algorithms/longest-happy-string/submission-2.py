class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []

        if a:
            maxHeap.append((-a, 'a'))
        if b:
            maxHeap.append((-b, 'b'))
        if c:
            maxHeap.append((-c, 'c'))

        heapq.heapify(maxHeap)

        res = ""
        while maxHeap:
            amount, letter = heapq.heappop(maxHeap)

            if len(res) >= 2 and res[-1] == letter and res[-2] == letter:
                if not maxHeap:
                    return res
                other_amount, other_letter = heapq.heappop(maxHeap)
                res += other_letter
                new_amount = other_amount + 1
                if new_amount < 0:
                    heapq.heappush(maxHeap, (new_amount, other_letter))
                heapq.heappush(maxHeap, (amount, letter))
            else:
                res += letter
                new_amount = amount + 1
                if new_amount < 0:
                    heapq.heappush(maxHeap, (new_amount, letter))
                
        return res