import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        vals = [-stone for stone in stones]
        heapq.heapify(vals)

        while len(vals) > 1:
            s1 = heapq.heappop(vals)
            s2 = heapq.heappop(vals)

            if s1 != s2:
                heapq.heappush(vals, -abs(s1-s2))

        return 0 if not vals else abs(vals[0])