from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        sol = nums[0]
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            sol = min(sol, nums[m])

            if nums[m] <= nums[r]:
                r = m - 1
            else:
                l = m + 1

        return min(sol, nums[l])