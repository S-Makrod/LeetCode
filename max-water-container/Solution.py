from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        j = len(heights) - 1
        i = 0
        area = 0

        while i < j:
            area = max(area, min(heights[i], heights[j]) * (j - i))

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return area

