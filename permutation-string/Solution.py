class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        counts = {}
        window = {}

        for char in s1:
            counts[char] = counts.get(char, 0) + 1

        for r in range(len(s2)):
            if s2[r] in counts:
                window[s2[r]] = window.get(s2[r], 0) + 1

                while window[s2[r]] > counts[s2[r]]:
                    window[s2[l]] = max(0, window[s2[l]] - 1)
                    l += 1

                if len(s1) == r - l + 1:
                    return True
            else:
                l = r + 1
                window = {}

        return False
