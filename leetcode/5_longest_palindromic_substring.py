class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = longest = 0
        for i in range(len(s)):
            left = i - longest - 1
            right = i + 1
            # check for palindrome extending window on both sides
            substring = s[left:right]
            if left >= 0 and substring == substring[::-1]:
                longest += 2
                start = left
            else:
                # check for palindrome extending window right only
                substring = s[left + 1:right]
                if substring == substring[::-1]:
                    longest += 1
                    start = left + 1
        return s[start:start + longest]
