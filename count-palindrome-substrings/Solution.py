class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindromeCount(l, r):
            sol = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                sol += 1
                l -= 1
                r += 1

            return sol

        sol = 0

        for i in range(len(s)):
            sol += palindromeCount(i, i)
            sol += palindromeCount(i, i + 1)

        return sol