from collections import deque

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        splat1, splat2 = deque(version1.split('.')), deque(version2.split('.'))
        while splat1 or splat2:
            if splat1:
                v1 = int(splat1.popleft())
            else:
                v1 = 0
            if splat2:
                v2 = int(splat2.popleft())
            else:
                v2 = 0
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1
        return 0
