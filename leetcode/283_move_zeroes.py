from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonzero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonzero], nums[i] = nums[i], nums[nonzero]
                nonzero += 1
