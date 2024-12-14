class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        m, n = len(word1), len(word2)
        for i in range(min(m, n)):
            answer.append(word1[i])
            answer.append(word2[i])
        if m < n:
            answer.append(word2[m:])
        elif n < m:
            answer.append(word1[n:])
        return ''.join(answer)
