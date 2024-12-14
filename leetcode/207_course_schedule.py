from typing import List
from collections import deque
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        heads = set(range(numCourses))
        incoming = [0] * numCourses
        outgoing = defaultdict(list)
        for course, prereq in prerequisites:
            incoming[course] += 1
            outgoing[prereq].append(course)
            if course in heads:
                heads.remove(course)
        heads = deque(heads)
        visited = 0
        while heads:
            node = heads.popleft()
            visited += 1
            for dest in outgoing[node]:
                incoming[dest] -= 1
                if incoming[dest] == 0:
                    heads.append(dest)
        return visited == numCourses
