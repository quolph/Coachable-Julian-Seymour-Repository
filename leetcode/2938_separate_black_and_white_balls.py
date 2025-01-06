class Solution:
    def minimumSteps(self, s: str) -> int:
        answer = zeroes = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                zeroes += 1
            else:
                answer += zeroes
        return answer
