from typing import List
from collections import deque

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        merged = -math.inf
        count = 0
        for start, end in sorted(points, key = lambda x : x[1]):
            if merged < start:
                count += 1
                merged = end
        return count
    def findMinArrowShotsSlow(self, points: List[List[int]]) -> int:
        start, end = 0, 1
        points = deque(sorted(points))
        merged = points.popleft()[end]
        count = 1
        while points:
            if points[0][start] <= merged:
                merged = min(merged, points[0][end])
                points.popleft()
            else:
                merged = points.popleft()[end]
                count += 1
        return count
