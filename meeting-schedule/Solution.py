from typing import List

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: (x.start, x.end))

        for i in range(1, len(intervals)):
            if max(intervals[i-1].start, intervals[i].start) < min(intervals[i-1].end, intervals[i].end):
                return False

        return True
