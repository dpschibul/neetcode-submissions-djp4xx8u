class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() # [[1,2],[1,4],[2,4]]
         
        removedCount = 0
        compared = intervals[0] # compared = [1,2]
        for i in range(1, len(intervals)):
            #    start 1           2.   interval[i] = [1,4]
            if intervals[i][0] >= compared[1]: 
                compared = intervals[i]
            else:
                removedCount += 1
                compared = intervals[i] if intervals[i][1] < compared[1] else compared
        
        return removedCount
