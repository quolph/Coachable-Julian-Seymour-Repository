class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        x1, y1, x2 = len(mat1[0]), len(mat1), len(mat2[0])
        answer = [[0] * x2 for _ in range(y1)]
        for j in range(y1):
            for i in range(x2):
                answer[j][i] = sum(mat1[j][p] * mat2[p][i] for p in range(x1))
        return answer
