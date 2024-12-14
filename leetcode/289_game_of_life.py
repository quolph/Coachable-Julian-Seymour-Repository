from collections import deque
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board[0]), len(board)
        def countLiveNeighbors(x: int, y: int) -> int:
            neighbors = 0
            for dx, dy in [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]:
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < m and 0 <= y2 < n and board[y2][x2] == 1:
                    neighbors += 1
                    if neighbors > 3:
                        break
            return neighbors
        kill, resurrect = deque(), deque()
        for y in range(n):
            for x in range(m):
                neighbors = countLiveNeighbors(x, y)
                if board[y][x] == 1 and (neighbors < 2 or neighbors > 3):
                    kill.append((x, y))
                elif board[y][x] == 0 and neighbors == 3:
                    resurrect.append((x, y))
        for x, y in kill:
            board[y][x] = 0
        for x, y in resurrect:
            board[y][x] = 1
