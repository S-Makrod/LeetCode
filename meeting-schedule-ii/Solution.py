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
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # if not intervals:
        #     return 0

        # sol = 1
        # intervals.sort(key=lambda x: (x.start, x.end))
        # days = [[intervals[0]]]

        # for i in range(1, len(intervals)):
        #     canFit = False
        #     for day in days:
        #         if not max(day[-1].start, intervals[i].start) < min(day[-1].end, intervals[i].end):
        #             canFit = True
        #             day.append(intervals[i])
        #             break

        #     if not canFit:
        #         sol += 1
        #         days.append([intervals[i]])

        # return sol
        overlaps = []

        for interval in intervals:
            overlaps.append((interval.start, 1))
            overlaps.append((interval.end, -1))

        overlaps.sort()

        curr = 0
        maxOverlaps = 0
        for _, val in overlaps:
            curr += val
            maxOverlaps = max(maxOverlaps, curr)

        return maxOverlaps
