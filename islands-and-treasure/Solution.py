from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        TREASURE = 0

        def dfs(i, j, dist):
            if i not in range(len(grid)) or j not in range(len(grid[0])) or grid[i][j] < dist:
                return

            grid[i][j] = dist
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for c, r in dirs:
                dfs(i+r, j+c, dist+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == TREASURE:
                    dfs(i, j, 0)
