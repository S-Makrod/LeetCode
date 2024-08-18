from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        squares = [[set(), set(), set()] for _ in range(3)]

        for i in range(9):
            row = board[i]

            for j in range(9):
                val = row[j]

                if val == '.':
                    continue

                if val in rows[i] or val in cols[j] or val in squares[i//3][j//3]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                squares[i//3][j//3].add(val)

        return True

