class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapp, mapq = {}, {}
        for i in range(len(s)):
            if s[i] not in mapp and t[i] not in mapq:
                mapp[s[i]] = t[i]
                mapq[t[i]] = s[i]
            elif s[i] in mapp and mapp[s[i]] != t[i] or t[i] in mapq and mapq[t[i]] != s[i]:
                return False
        return True
