class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = {}
        size = 0
        start = 0

        for i in range(len(s)):
            char = s[i]
            size = max(size, i - start)

            if seen_chars.get(char, -1) >= start:
                start = seen_chars[char] + 1

            seen_chars[char] = i

        return max(size, len(s) - start)
