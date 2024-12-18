import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.limit = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.limit:
            heapq.heappush(self.heap, val)
        elif self.heap[0] < val:
            heapq.heappushpop(self.heap, val)

        return self.heap[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif heap[0] < num:
                heapq.heappushpop(heap, num)

        return heap[0]

