from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n, answer = len(citations), 0
        for i, value in enumerate(citations):
            if value + i - 1 >= n:
                answer = max(answer, len(citations) - i)
            elif citations[value + i - 1] >= value:
                answer = value
        return answer
