import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            priority = - ((x ** 2 + y ** 2) ** .5)

            if len(heap) < k:
                heapq.heappush(heap, (priority, [x, y]))
            elif heap[0][0] < priority:
                heapq.heappushpop(heap, (priority, [x, y]))

        return [point for _, point in heap]