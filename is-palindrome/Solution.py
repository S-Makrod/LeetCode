class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ''
        reverse = ''

        for char in s:
            if char.isalnum():
                forward += char.lower()
                reverse = char.lower() + reverse

        return forward == reverse
