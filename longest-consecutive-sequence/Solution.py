from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = sorted(nums)
        sol = [1 for _ in range(len(vals))]

        for i in range(len(vals)):
            if i == 0:
                continue

            if vals[i-1] + 1 == vals[i]:
                sol[i] += sol[i-1]
            if vals[i-1] == vals[i]:
                sol[i] = sol[i-1]

        return max(sol, default=0)
