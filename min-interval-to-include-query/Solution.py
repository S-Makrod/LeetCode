import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sorted_queries = sorted(queries)
        intervals.sort()
        heap = []
        query_map = {}
        i = 0

        for q in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(heap, (e - s + 1, e))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            query_map[q] = heap[0][0] if heap else -1

        return [query_map[query] for query in queries]
