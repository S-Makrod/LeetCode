class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindromeLength(l, r):
            res = ""
            resLen = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            return res

        res = ""
        resLen = 0

        for i in range(len(s)):
            pal = palindromeLength(i, i)
            if len(pal) > len(res):
                res = pal

            pal = palindromeLength(i, i + 1)
            if len(pal) > len(res):
                res = pal

        return res