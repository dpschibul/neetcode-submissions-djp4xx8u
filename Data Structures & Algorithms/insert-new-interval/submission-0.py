class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for interval in intervals: 
            if not newInterval or newInterval[0] > interval[1]:
                res.append(interval)
                continue
            
            if newInterval and newInterval[1] < interval[0]: 
                res.append(newInterval)
                res.append(interval)
                newInterval = None
                continue

            if newInterval[0] <= interval[1] and newInterval[1] >= interval[0]:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])] # new_interval = 1, 6
            
        if newInterval:
            res.append(newInterval)

        return res
