from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0

        while i < len(nums) - 1:
            jump = nums[i]

            if jump == 0:
                break

            end = min(i + jump, len(nums) - 1)
            i += 1
            j = i
            while j <= end and j < len(nums):
                if j + nums[j] >= i + nums[i]:
                    i = j
                j += 1

        return i >= len(nums) - 1