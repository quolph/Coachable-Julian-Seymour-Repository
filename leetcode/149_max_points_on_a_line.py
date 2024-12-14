from typing import List
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        answer = 1
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            slopes = defaultdict(int)
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 == x2:
                    key = x1
                else:
                    slope = (y2 - y1)/(x2 - x1)
                    y_intercept = y1 - slope * x1
                    key = ((slope, y_intercept))
                slopes[key] += 1
            answer = max(answer, max(slopes.values()) + 1)
        return answer
    def maxPointsSlow(self, points: List[List[int]]) -> int:
        lines = defaultdict(set)
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 == x2:
                    lines[x1].add((x1, y1))
                    lines[x1].add((x2, y2))
                else:
                    slope = (y2 - y1)/(x2 - x1)
                    y_intercept = y1 - slope * x1
                    lines[(slope, y_intercept)].add((x1, y1))
                    lines[(slope, y_intercept)].add((x2, y2))
        answer = 1
        for key, values in lines.items():
            answer = max(answer, len(values))
        return answer
