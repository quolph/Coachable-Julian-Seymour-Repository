from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current = nums[0]
        for num in nums[1:]:
            current += num
            if num > current:
                current = num
            if current > max_sum:
                max_sum = current
        return max_sum
    def maxSubArraySlow(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [None] * n
        memo[0] = nums[0]
        m = nums[0]
        i = 1
        while i < n:
            memo[i] = nums[i] + max(memo[i-1], 0)
            m = max(m, memo[i])
            i += 1
        return m
