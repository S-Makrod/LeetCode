from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sol = []
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            val = digits[i]

            if val == 9 and carry:
                val = 0
            else:
                val += carry
                carry = 0

            sol.insert(0, val)

        if carry:
            sol.insert(0, 1)

        return sol
