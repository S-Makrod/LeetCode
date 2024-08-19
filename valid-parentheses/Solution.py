class Solution:
    def isValid(self, s: str) -> bool:
        keys = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        stack = []

        for char in s:
            if char not in keys:
                stack.append(char)
            elif len(stack) == 0 or keys[char] != stack.pop():
                return False

        return len(stack) == 0
