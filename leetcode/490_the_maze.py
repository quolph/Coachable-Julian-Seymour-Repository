class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze[0]), len(maze)
        x, y = start[1], start[0]
        queue = collections.deque([(x, y)])
        visited = set()
        while queue:
            x, y = queue.popleft()
            if (x, y) in visited:
                continue
            if x == destination[1] and y == destination[0]:
                return True
            #up
            y2 = y - 1
            if y2 >= 0 and maze[y2][x] != 1:
                while y2 > 0 and maze[y2 - 1][x] != 1:
                    y2 -= 1
                if (x, y2) not in visited:
                    queue.append((x, y2))
            #down
            y2 = y + 1
            if y2 < n and maze[y2][x] != 1:
                while y2 < n - 1 and maze[y2 + 1][x] != 1:
                    y2 += 1
                if (x, y2) not in visited:
                    queue.append((x, y2))
            #left
            x2 = x - 1
            if x2 >= 0 and maze[y][x2] != 1:
                while x2 > 0 and maze[y][x2 - 1] != 1:
                    x2 -= 1
                if (x2, y) not in visited:
                    queue.append((x2, y))
            #right
            x2 = x + 1
            if x2 < m and maze[y][x2] != 1:
                while x2 < m - 1 and maze[y][x2 + 1] != 1:
                    x2 += 1
                if (x2, y) not in visited:
                    queue.append((x2, y))
            visited.add((x, y))
        return False

