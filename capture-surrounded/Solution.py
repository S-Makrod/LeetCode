from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(i, j):
            if not 0 <= i < ROWS or not 0 <= j < COLS or board[i][j] != 'O':
                return

            board[i][j] = 'C'

            for d1, d2 in dirs:
                dfs(i + d1, j + d2)

        for i in [0, ROWS - 1]:
            for j in range(COLS):
                if board[i][j] == 'O':
                    dfs(i, j)

        for j in [0, COLS - 1]:
            for i in range(ROWS):
                if board[i][j] == 'O':
                    dfs(i, j)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'C':
                    board[i][j] = 'O'
