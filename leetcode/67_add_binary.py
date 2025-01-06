from collections import deque

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        carry = 0
        answer = deque()
        for i in range(n):
            j = len(a) - i - 1
            k = len(b) - i - 1
            if j < 0:
                v1 = 0
            else:
                v1 = int(a[j])
            if k < 0:
                v2 = 0
            else:
                v2 = int(b[k])
            v3 = v1 + v2 + carry
            if v3 % 2 == 0:
                answer.appendleft('0')
            else:
                answer.appendleft('1')
            if v3 > 1:
                carry = 1
            else:
                carry = 0
        if carry == 1:
            answer.appendleft('1')
        return ''.join(answer)
