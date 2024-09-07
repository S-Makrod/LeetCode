from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        t = 0
        b = len(heights)
        l = 0
        r = len(heights[0])
        down = [[0, 1], [1, 0], [0, -1]]
        up = [[0, -1], [-1, 0], [0, 1]]

        sol = []
        atlantic = set()
        pacific = set()
        queue = [(i, r - 1) for i in range(b)] + [(b - 1, i) for i in range(r)]

        while queue:
            i, j = queue.pop(0)
            atlantic.add((i, j))

            for dirs in up:
                d1 = i + dirs[0]
                d2 = j + dirs[1]

                if t <= d1 < b and l <= d2 < r and heights[d1][d2] >= heights[i][j] and (d1, d2) not in atlantic:
                    queue.append((d1, d2))

        queue = [(i, l) for i in range(b)] + [(t, i) for i in range(r)]

        while queue:
            i, j = queue.pop(0)
            pacific.add((i, j))

            for dirs in down:
                d1 = i + dirs[0]
                d2 = j + dirs[1]

                if t <= d1 < b and l <= d2 < r and heights[d1][d2] >= heights[i][j] and (d1, d2) not in pacific:
                    queue.append((d1, d2))

        for val in atlantic:
            if val in pacific:
                sol.append([val[0], val[1]])

        return sol