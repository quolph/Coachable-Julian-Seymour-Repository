class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                fail = False
                for j in range(1, len(needle)):
                    if haystack[i + j] != needle[j]:
                        fail = True
                        break
                if not fail:
                    return i
        return -1
