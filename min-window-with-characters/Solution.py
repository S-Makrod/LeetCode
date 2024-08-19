class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        counts = {}
        window = {}

        for char in t:
            counts[char] = counts.get(char, 0) + 1

        for r in range(len(s)):
            if s[l] not in counts:
                l = r + 1
                continue

            window[s[r]] = window.get(s[r], 0) + 1

            while window[s[l]] > counts.get(s[l], 0) or s[l] not in counts:
                window[s[l]] = max(0, window[s[l]] - 1)
                l += 1

        while r >= 0 and s[r] not in counts:
            r -= 1

        for char in s[l:r+1]:
            if char in counts:
                counts[char] -= 1
                if counts[char] == 0:
                    del counts[char]

        return '' if bool(counts) else s[l:r+1]