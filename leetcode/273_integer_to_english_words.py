from collections import deque

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        words = [
            "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
            "Eighteen", "Nineteen", "Twenty"
        ]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        def helper(remainder: int) -> str:
            ret = []
            if remainder//100 != 0:
                ret.append(words[remainder//100])
                ret.append("Hundred")
                remainder %= 100
            if 0 < remainder < 21:
                ret.append(words[remainder])
            else:
                if remainder//10 != 0:
                    ret.append(tens[remainder//10])
                    remainder %= 10
                if remainder != 0:
                    ret.append(words[remainder])
            return ' '.join(ret)
        magnitude = 0
        answer = deque()
        while num > 0:
            if num % 1000 != 0:
                if magnitude > 0:
                    answer.appendleft(thousands[magnitude])
                answer.appendleft(helper(num % 1000))
            num //= 1000
            magnitude += 1
        return ' '.join(answer)
