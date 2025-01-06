from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        while i < len(intervals) - 1:
            if intervals[i + 1][0] <= intervals[i][1]: # if there is a collision,
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1]) # then merge the intervals
                intervals.pop(i + 1)
            else: # otherwise, increment i
                i += 1
        return intervals
