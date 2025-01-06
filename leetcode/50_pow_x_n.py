class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0 or x == 1 or n == 1:
            return x
        answer = self.myPow(x, abs(n)//2)
        answer *= answer
        if n % 2 != 0:
            answer *= x
        if n < 0:
            return 1/answer
        return answer
