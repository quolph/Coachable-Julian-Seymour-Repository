from typing import List
from collections import deque

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board[0]), len(board)
        def bfs(queue):
            while queue:
                x, y = queue.popleft()
                if board[y][x] == 'B':
                    continue
                mine_count = 0
                new_queue = deque()
                for dx, dy in [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]:
                    x2, y2 = x + dx, y + dy
                    if 0 <= x2 < m and 0 <= y2 < n:
                        if board[y2][x2] == 'M':
                            mine_count += 1
                            new_queue = None
                        elif board[y2][x2] == 'E' and mine_count == 0:
                            new_queue.append((x2, y2))
                if mine_count == 0:
                    board[y][x] = 'B'
                    queue.extend(new_queue)
                else:
                    board[y][x] = str(mine_count)
        y, x = click
        if board[y][x] == 'M':
            board[y][x] = 'X'
        elif board[y][x] == 'E':
            bfs(deque([(x, y)]))
        return board
