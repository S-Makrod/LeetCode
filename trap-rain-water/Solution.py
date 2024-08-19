from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        i = 0
        j = len(height) - 1
        max_left = height[i]
        max_right = height[j]
        area = 0

        while i < j:
            if height[i] > height[j]:
                max_right = max(max_right, height[j])
                area += max_right - height[j]
                j -= 1
            else:
                max_left = max(max_left, height[i])
                area += max_left - height[i]
                i += 1

        return area
