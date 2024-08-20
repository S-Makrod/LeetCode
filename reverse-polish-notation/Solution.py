from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_eval = {
            '-': lambda x, y: x - y,
            '+': lambda x, y: x + y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: 0 if x == 0 else int(x / y)
        }

        ops = []
        nums = []
        val = None

        for token in tokens:
            if token not in op_eval:
                nums.append(int(token))
            else:
                v1 = nums.pop()
                v2 = nums.pop()
                val = op_eval[token](v2, v1)
                nums.append(val)

        return val if val is not None else nums.pop()
