from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        min_x, max_x = 0, len(matrix[0]) - 1
        min_y, max_y = 0, len(matrix) - 1
        spiral = []
        while min_x <= max_x and min_y <= max_y:
            if min_x == max_x:
                for y in range(min_y, max_y + 1):
                    spiral.append(matrix[y][min_x])
            elif min_y == max_y:
                for x in range(min_x, max_x + 1):
                    spiral.append(matrix[min_y][x])
            else:
                for x in range(min_x, max_x):
                    spiral.append(matrix[min_y][x])
                for y in range(min_y, max_y):
                    spiral.append(matrix[y][max_x])
                for x in range(max_x, min_x, -1):
                    spiral.append(matrix[max_y][x])
                for y in range(max_y, min_y, -1):
                    spiral.append(matrix[y][min_x])
            min_x += 1
            max_x -= 1
            min_y += 1
            max_y -= 1
        return spiral
