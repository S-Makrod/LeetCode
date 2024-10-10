from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def robHelper(nums: List[int]) -> int:
            if not nums:
                return 0

            max_include = nums[0]
            max_not_include = 0

            for i in range(1, len(nums)):
                temp = max_include
                max_include = nums[i] + max_not_include
                max_not_include = max(temp, max_not_include)

            return max(max_include, max_not_include)

        return max(nums[0], robHelper(nums[:-1]), robHelper(nums[1:]))