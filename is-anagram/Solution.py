class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False
            count[char] -= 1

            if count[char] == 0:
                del count[char]

        return not count

