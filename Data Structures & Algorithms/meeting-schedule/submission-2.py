"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# [(0,5),(5,10),(15,20), (19, 22)]
#.     5 >5, 10 > 15, 20 > 19 -> return false`
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)

        tmpEnd = intervals[0].end

        for interval in intervals[1:]:
            if tmpEnd > interval.start:
                return False
            tmpEnd = interval.end

        return True


