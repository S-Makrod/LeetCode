# from queue import Queue

class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 0:
        #     return 0

        # steps = {}
        # steps[0] = 1

        # for i in range(1, n):
        #     steps[i] = steps.get(i - 1, 0) + steps.get(i - 2, 0)

        # return steps.get(n - 1, 0) + steps.get(n - 2, 0)

        if n <= 2:
            return n

        n1 = 1
        n2 = 2

        for i in range(3, n):
            temp = n2
            n2 = n1 + n2
            n1 = temp

        return n1 + n2