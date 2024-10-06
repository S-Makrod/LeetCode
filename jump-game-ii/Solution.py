from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        jump_count = 0

        while i < len(nums) - 1:
            jump = nums[i]
            end = min(i + jump, len(nums) - 1)

            if end == len(nums) - 1:
                jump_count += 1
                break

            i += 1
            j = i

            while j <= end and j < len(nums):
                if j + nums[j] >= i + nums[i]:
                    i = j
                j += 1

            jump_count += 1

        return jump_count