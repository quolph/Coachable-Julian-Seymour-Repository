class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        answer = []
        a_count, b_count, c_count = 0, 0, 0
        length = a + b + c
        for i in range(length):
            if a > 0 and a_count < 2 and (a >= b and a >= c or b_count == 2 or c_count == 2):
                a -= 1
                a_count += 1
                b_count = c_count = 0
                answer.append('a')
            elif b > 0 and b_count < 2 and (b >= a and b >= c or a_count == 2 or c_count == 2):
                b -= 1
                b_count += 1
                a_count = c_count = 0
                answer.append('b')
            elif c > 0 and c_count < 2 and (c >= a and c >= b or a_count == 2 or b_count == 2):
                c -= 1
                c_count += 1
                a_count = b_count = 0
                answer.append('c')
            else:
                break
        return ''.join(answer)
