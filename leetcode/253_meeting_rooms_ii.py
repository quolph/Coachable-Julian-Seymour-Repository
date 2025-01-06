from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        meetings = []
        rooms = 0
        intervals.sort()
        for start, end in intervals:
            if meetings and start >= meetings[0]:
                heapq.heappop(meetings)
            else:
                rooms += 1
            heapq.heappush(meetings, end)
        return rooms
