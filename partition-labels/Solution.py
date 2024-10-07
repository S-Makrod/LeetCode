from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # last_seen = {}

        # for i in range(len(s)):
        #     last_seen[s[i]] = i

        # curr = set(s[0])
        # sol = []
        # start = 0

        # for i in range(1, len(s)):
        #     clear = True

        #     for char in curr:
        #         if last_seen[char] >= i:
        #             clear = False

        #     if clear:
        #         sol.append(i - start)
        #         start = i
        #         curr = set()

        #     curr.add(s[i])

        # sol.append(i - start + 1)
        # return sol

        last_seen = {}

        for i in range(len(s)):
            last_seen[s[i]] = i

        curr = 0
        target = 0
        sol = []

        for i in range(len(s)):
            target = max(last_seen[s[i]], target)
            curr += 1

            if i == target:
                sol.append(curr)
                curr = 0

        return sol