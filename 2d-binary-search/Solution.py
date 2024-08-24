from typing import List

class Solution:
    def search(self, nums: List[int], target: int, comp: callable) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            val = comp(target, nums[m])

            if val == 0:
                return m
            elif val > 0:
                r = m - 1
            else:
                l = m + 1

        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = self.search(matrix, target,
            lambda t, row: 0 if row[0] <= t <= row[-1] else (-1 if t > row[0] else 1))

        return self.search(matrix[index], target,
            lambda t, v: 0 if t == v else (-1 if t > v else 1)) != -1
