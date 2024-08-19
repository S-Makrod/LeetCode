class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # k_used = 0
        # k_pos = -1
        # sol = 0
        # curr = 0
        # i = 0
        # char = i

        # while i < len(s):
        #     if s[char] == s[i]:
        #         curr += 1
        #         i += 1
        #     else:
        #         if k_used == k:
        #             if k_pos != -1:
        #                 i = k_pos
        #             char = i
        #             k_used = 0
        #             k_pos = -1
        #             curr = 0
        #         else:
        #             k_used += 1
        #             curr += 1
        #             if k_pos == -1:
        #                 k_pos = i
        #             i += 1

        #     sol = max(sol, curr)

        # return min(len(s), sol + k - k_used)

        counts = {}
        maxfreq = 0
        l = 0

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            maxfreq = max(maxfreq, counts[s[r]])

            while r - l + 1 - maxfreq > k:
                counts[s[l]] -= 1
                l += 1


        return r - l + 1
