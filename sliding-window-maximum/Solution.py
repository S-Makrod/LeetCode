import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        sol = []
        heap = []
        l = 0
        largest = float('-inf')

        for r in range(0, len(nums)):
            heapq.heappush(heap, (-nums[r], -r))

            if nums[r] >= largest:
                largest = nums[r]
                l = r
            else:
                while not (r - k < l):
                    largest, l = heapq.heappop(heap)
                    l = -l
                    largest = -largest

            if (r + 1 >= k):
                sol.append(largest)

        return sol

        # original idea, optimized to merge both loops above

        # sol = []
        # heap = []

        # l = 0
        # largest = float('-inf')

        # for r in range(0, k):
        #     if nums[r] >= largest:
        #         l = r
        #         largest = nums[r]
        #     heapq.heappush(heap, (-nums[r], -r))

        # sol.append(largest)

        # for r in range(k, len(nums)):
        #     if nums[r] >= largest:
        #         sol.append(nums[r])
        #         largest = nums[r]
        #         l = r
        #     else:
        #         heapq.heappush(heap, (-nums[r], -r))

        #         if r - k < l:
        #             sol.append(largest)
        #         else:
        #             while not (r - k < l):
        #                 largest, l = heapq.heappop(heap)
        #                 l = -l
        #                 largest = -largest

        #             sol.append(largest)

        # return sol
