import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        sol = 0

        while l <= r:
            m = l + ((r - l) // 2)

            count = 0
            for val in piles:
                count += math.ceil(val/m)

            if count <= h:
                sol = m
                r = m - 1
            else:
                l = m + 1

        return sol
