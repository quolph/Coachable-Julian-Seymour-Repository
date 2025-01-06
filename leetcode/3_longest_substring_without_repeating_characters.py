class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length = 0
        for right in range(len(s)): # iterate from left to right
            if s[left:right].count(s[right]) == 0: # if the string between the left and right indices contains no duplicates,
                length = max(length, right - left + 1) # update the max length
            else: # otherwise move left index up to the first occurence of the character on the right
                left += s[left:right].index(s[right]) + 1
        return length
