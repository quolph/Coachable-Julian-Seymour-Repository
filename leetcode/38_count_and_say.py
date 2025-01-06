class Solution:
    def countAndSay(self, n: int) -> str:
        prev = [1]
        for i in range(2, n + 1):
            encoding = []
            count = 1
            for j in range(1, len(prev)):
                if prev[j] == prev[j - 1]:
                    count += 1
                else:
                    encoding.append(count)
                    encoding.append(prev[j - 1])
                    count = 1
            encoding.append(count)
            encoding.append(prev[-1])
            prev = encoding
        answer = []
        for digit in prev:
            answer.append(str(digit))
        return ''.join(answer)
    def countAndSaySlow(self, n: int) -> str:
        if n == 1:
            return "1"
        k = 1
        p = 1
        while k < n:
            pairs = collections.deque()
            prev = None
            count = 1
            while p > 0:
                digit = p % 10
                if digit == prev:
                    count += 1
                else:
                    if prev is not None:
                        pairs.appendleft((count, prev))
                    count = 1
                    prev = digit
                p //= 10
            pairs.appendleft((count, digit))
            p = 0
            while pairs:
                count, digit = pairs.popleft()
                p = p * 100 + 10 * count + digit
            k += 1
        answer = collections.deque()
        while p > 0:
            answer.appendleft(str(p % 10))
            p //= 10
        return ''.join(answer)
