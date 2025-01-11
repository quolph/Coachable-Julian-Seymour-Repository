class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        tuples = []
        for y, row in enumerate(nums):
            for x, num in enumerate(row):
                tuples.append((x + y, x, num))
        tuples.sort()
        return [tuples[i][2] for i in range(len(tuples))]
    def findDiagonalOrderSlow(self, nums: List[List[int]]) -> List[int]:
        m, n = max(len(nums[i]) for i in range(len(nums))), len(nums)
        answer = []
        for y in range(n):
            x = 0
            y2 = y
            while y2 >= 0:
                if x < len(nums[y2]):
                    answer.append(nums[y2][x])
                y2 -= 1
                x += 1
        for x in range(1, m):
            y = n - 1
            x2 = x
            while y >= 0 and x2 < m:
                if x2 < len(nums[y]):
                    answer.append(nums[y][x2])
                y -= 1
                x2 += 1
        return answer
