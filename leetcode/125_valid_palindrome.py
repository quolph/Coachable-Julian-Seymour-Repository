class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = []
        for char in s:
            if char.isalnum():
                alphanumeric.append(char.lower())
        alphanumeric = ''.join(alphanumeric)
        return alphanumeric == alphanumeric[::-1]
