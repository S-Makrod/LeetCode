from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # steps = {}
        # steps[0] = 0
        # steps[1] = 0

        # for i in range(2, len(cost)):
        #     v1 = float('inf')
        #     v2 = float('inf')

        #     if i - 1 in steps:
        #         v1 = steps[i-1] + cost[i-1]
        #     if i - 2 in steps:
        #         v2 = steps[i-2] + cost[i-2]

        #     steps[i] = min(v1, v2)

        # return min(steps[len(cost) - 1] + cost[len(cost) - 1], steps[len(cost) - 2] + cost[len(cost) - 2])

        c1 = 0
        c2 = 0

        for i in range(2, len(cost)):
            temp = c1
            c1 = min(c1 + cost[i - 1], c2 + cost[i - 2])
            c2 = temp

        return min(c1 + cost[len(cost) - 1], c2 + cost[len(cost) - 2])
