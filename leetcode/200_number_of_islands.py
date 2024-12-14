from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_x, max_y = len(grid[0]), len(grid)
        def dfs(x: int, y: int) -> None:
            grid[y][x] = "0"
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < max_x and 0 <= y2 < max_y and grid[y2][x2] == "1":
                    dfs(x2, y2)
        islands = 0
        for y in range(max_y):
            for x in range(max_x):
                if grid[y][x] == "1":
                    islands += 1
                    dfs(x, y)
        return islands
