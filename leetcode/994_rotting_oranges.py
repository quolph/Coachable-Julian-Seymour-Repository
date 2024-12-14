from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, rotten = 1, 2
        width, height = len(grid[0]), len(grid)
        queue, next_queue = deque(), deque()
        oranges, minutes = 0, 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == fresh:
                    oranges += 1
                elif grid[y][x] == rotten:
                    queue.append((x, y))
        while queue and oranges > 0:
            while queue and oranges > 0:
                x, y = queue.popleft()
                for offset_x, offset_y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    x2, y2 = x + offset_x, y + offset_y
                    if y2 < 0 or y2 == height or x2 < 0 or x2 == width or grid[y2][x2] != fresh:
                        continue
                    next_queue.append((x2, y2))
                    grid[y2][x2] = rotten
                    oranges -= 1
            queue, next_queue = next_queue, deque()
            minutes += 1
        if oranges == 0:
            return minutes
        return -1
