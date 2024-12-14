from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        left[0] = 1
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            left[i] *= product
            product *= nums[i]
        return left
