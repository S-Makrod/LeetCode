from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sol = 0
        intervals.sort()
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            s, e = intervals[i]

            if max(s, start) < min(e, end):
                sol += 1

                if end > e:
                    end = e
                    start = s
            else:
                start = s
                end = e


        return sol