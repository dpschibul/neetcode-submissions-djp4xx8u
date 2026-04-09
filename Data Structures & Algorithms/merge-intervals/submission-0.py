class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]

        for start, end in intervals[1:]:
            if res[-1][1] < start:
                res.append([start, end])
            else:
                merged = [res[-1][0], max(end, res[-1][1])]
                res.pop()
                res.append(merged)
        return res

        