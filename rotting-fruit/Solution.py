from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottenMap = [[float('inf')]*len(grid[0]) for _ in range(len(grid))]

        def dfs(i, j, time):
            if i not in range(len(grid)) or j not in range(len(grid[0])) or grid[i][j] == 0 or rottenMap[i][j] < time:
                return

            rottenMap[i][j] = time
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for c, r in dirs:
                dfs(i+r, j+c, time+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottenMap[i][j] = 0
                    dfs(i, j, 0)

                if grid[i][j] == 0:
                    rottenMap[i][j] = 0

        time = max([max(rottenMap[i]) for i in range(len(rottenMap))])
        return -1 if time == float('inf') else time
