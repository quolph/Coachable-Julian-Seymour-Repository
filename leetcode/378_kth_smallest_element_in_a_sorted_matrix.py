class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        m, n = len(matrix[0]), len(matrix)
        for j in range(n):
            for i in range(m):
                if len(heap) == k:
                    popped = heapq.heappushpop(heap, -matrix[j][i])
                else:
                    heapq.heappush(heap, -matrix[j][i])
        return -heap[0]
