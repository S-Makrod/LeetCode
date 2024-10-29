from collections import Counter
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = []

        for task, count in counter.items():
            heapq.heappush(heap, (0, -count, task))

        currtime = 1

        while heap:
            time, count, val = heapq.heappop(heap)

            if time < currtime:
                heapq.heappush(heap, (currtime, count, val))
                continue

            currtime = max(currtime, time)
            count += 1

            if count != 0:
                heapq.heappush(heap, (currtime + n + 1, count, val))
            elif len(heap) == 0:
                return currtime

            currtime += 1

        return 0