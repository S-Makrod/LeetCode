from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x = len(grid[0])
        y = len(grid)

        count = 0
        visit = set()

        def dfs(i, j):
            if (i, j) in visit or not 0 <= i < y or not 0 <= j < x or grid[i][j] == '0':
                return

            visit.add((i, j))
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for c, r in dirs:
                dfs(i+r, j+c)

        for i in range(y):
            for j in range(x):
                if (i, j) not in visit and grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count
