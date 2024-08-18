from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = {}

        for s in strs:
            key = ''.join(sorted(s))
            sol.setdefault(key, []).append(s)

        return sol.values()
