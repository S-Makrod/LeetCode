from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        cs = 0
        ce = len(matrix[0])
        rs = 0
        re = len(matrix)
        sol = []

        while cs < ce and rs < re:
            for i in range(cs, ce):
                sol.append(matrix[rs][i])

            rs += 1
            for i in range(rs, re):
                sol.append(matrix[i][ce - 1])

            ce -= 1
            if not (rs < re and cs < ce):
                break

            for i in range(ce - 1, cs - 1, -1):
                sol.append(matrix[re - 1][i])

            re -= 1
            for i in range(re - 1, rs - 1, -1):
                sol.append(matrix[i][cs])

            cs += 1

        return sol
