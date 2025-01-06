class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {"I":1, "V":5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i, answer = len(s) - 1, 0
        while i >= 0:
            value = symbols[s[i]]
            answer += value
            if i > 0:
                prev = symbols[s[i - 1]]
                if value > prev:
                    answer -= prev
                    i -= 2
                else:
                    i -= 1
            else:
                i -= 1
        return answer
    def romanToInt2(self, s: str) -> int:
        symbols = {"I":1, "V":5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev = answer = 0
        for char in s:
            value = symbols[char]
            answer += value
            if prev > 0 and value > prev:
                answer -= 2 * prev
            prev = value
        return answer
