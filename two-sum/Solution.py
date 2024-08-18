from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in num_dict:
                return [num_dict[num], i]

            num_dict[target - num] = i

        return None