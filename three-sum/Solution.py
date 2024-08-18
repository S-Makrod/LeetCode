from collections import defaultdict
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        twosum = defaultdict(list)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                twosum[nums[i] + nums[j]].append([i, j])

        sol = set()

        for i in range(len(nums)):
            if 0 - nums[i] in twosum:
                for pair in twosum[0 - nums[i]]:
                    if i not in pair:
                        sol.add(
                            tuple(sorted([nums[i], nums[pair[0]], nums[pair[1]]]))
                        )

        return [list(item) for item in sol]