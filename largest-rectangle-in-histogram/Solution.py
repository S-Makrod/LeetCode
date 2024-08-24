from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for height in heights:
            stack.append((0, height))
            areas = []

            while stack:
                area, bound = stack.pop()

                if height >= bound:
                    area += bound
                else:
                    area = (area // bound + 1) * height
                    bound = height

                max_area = max(max_area, area)
                areas.append((area, bound))

            stack = areas

        return max_area
