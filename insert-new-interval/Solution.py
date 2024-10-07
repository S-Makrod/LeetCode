from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        sol = []
        start, end = newInterval[0], newInterval[1]

        for i in range(len(intervals)):
            s, e = intervals[i]

            if max(s, start) <= min(e, end):
                start = min(s, start)
                end = max(e, end)
            elif end < s:
                sol.append([start, end])
                return sol + intervals[i:]
            else:
                sol.append([s, e])

        sol.append([start, end])
        return sol
