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
        
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                meeting_count+=1
                s+=1
            else:
                meeting_count-=1
                e+=1
            
            max_meetings=max(max_meetings, meeting_count)


        return max_meetings
        