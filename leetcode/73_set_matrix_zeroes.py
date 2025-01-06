from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        width, height = len(matrix[0]), len(matrix)
        row1 = column1 = False
        # determine whether the first row contains a 0
        for x in range(width):
            if matrix[0][x] == 0:
                row1 = True
                break
        # determine whether the first column contains a 0
        for y in range(height):
            if matrix[y][0] == 0:
                column1 = True
                break
        # flag all rows and columns with 0s in them
        for y in range(1, height):
            for x in range(1, width):
                if matrix[y][x] == 0:
                    matrix[0][x] = 0
                    matrix[y][0] = 0
        # iterate through all x, y starting at 1, 1 and set their contents to 0
        for y in range(1, height):
            for x in range(1, width):
                if matrix[y][0] == 0 or matrix[0][x] == 0:
                    matrix[y][x] = 0
        # deal with first row
        if row1:
            for x in range(width):
                matrix[0][x] = 0
        # deal with first column
        if column1:
            for y in range(height):
                matrix[y][0] = 0
