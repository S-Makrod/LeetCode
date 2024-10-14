class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)
            total = 0

            while n > 0:
                digit = n % 10
                n = n // 10

                total += digit ** 2

            n = total

        return True
