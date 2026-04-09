"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()
        meeting_count=0
        max_meetings=0
        
        while start:
            if start[0] < end[0]:
                meeting_count+=1
                start.pop(0)
            else:
                meeting_count-=1
                end.pop(0)
            max_meetings=max(max_meetings, meeting_count)


        return max_meetings
        