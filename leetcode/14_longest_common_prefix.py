from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        length = min(len(string) for string in strs)
        s1 = strs[0]
        for i in range(length):
            for j in range(1, len(strs)):
                s2 = strs[j]
                if s1[i] != s2[i]:
                    return s1[:i]
        return s1[:length]
