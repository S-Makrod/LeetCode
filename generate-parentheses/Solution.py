from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        queue = [('(', 0, 1)] # go by single ( increment n on close
        sol = set()

        while queue:
            val, k, open_parentheses = queue.pop()

            if k != n:
                vals = set()
                if open_parentheses > 0:
                    vals.add((val + ')', k + 1, open_parentheses - 1))
                if k + open_parentheses < n:
                    vals.add((val + '(', k, open_parentheses + 1))
                queue.extend(vals)
            else:
                sol.add(val)

        return list(sol)

