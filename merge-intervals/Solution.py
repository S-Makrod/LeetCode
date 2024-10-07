from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sol = []
        intervals.sort()
        start, end = intervals[0]

        for i in range(len(intervals)):
            s, e = intervals[i]

            if max(s, start) <= min(e, end):
                start = min(s, start)
                end = max(e, end)
            else:
                sol.append([start, end])
                start = s
                end = e

        sol.append([start, end])
        return sol