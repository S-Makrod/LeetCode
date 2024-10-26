from copy import deepcopy
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = [[]]

        for num in nums:
            temp = deepcopy(sol)

            for val in temp:
                val.append(num)
                sol.append(val)

        return sol
