from typing import List

class Solution:
    # assumes numbers is sorted and non-decreasing
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while True:
            res = numbers[i] + numbers[j]

            if res > target:
                j -= 1
            elif res < target:
                i += 1
            else:
                return [i + 1, j + 1]
