from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        x = len(grid[0])
        y = len(grid)

        maxArea = 0
        visit = set()

        def dfs(i, j):
            if (i, j) in visit or not 0 <= i < y or not 0 <= j < x or grid[i][j] == 0:
                return 0

            size = 1
            visit.add((i, j))
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for c, r in dirs:
                size += dfs(i+r, j+c)

            return size

        for i in range(y):
            for j in range(x):
                if (i, j) not in visit and grid[i][j] == 1:
                    area = dfs(i, j)
                    maxArea = max(area, maxArea)

        return maxArea