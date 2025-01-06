from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        previous = -101
        index = 0
        for j, num in enumerate(nums):
            if num > previous:
                nums[index] = num
                previous = num
                index += 1
        return index
