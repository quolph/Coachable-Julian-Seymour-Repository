from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer, combo = [], []
        def helper(i: int):
            if len(combo) == k:
                answer.append(combo.copy())
                return
            if k - len(combo) < i:
                helper(i - 1)
            combo.append(i)
            helper(i - 1)
            combo.pop()
        helper(n)
        return answer
    def combineSlow(self, n: int, k: int) -> List[List[int]]:
        answer = []
        if k == 1:
            for i in range(1, n + 1):
                answer.append([i])
        else:
            for combo in self.combine(n, k - 1):
                for i in range(combo[-1] + 1, n + 1):
                    answer.append(combo + [i])
        return answer
