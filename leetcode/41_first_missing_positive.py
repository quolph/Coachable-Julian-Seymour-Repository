from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # needed for arrays without missing positives from 1 to n
        nums.append(0)
        n = len(nums)
        # get rid of all values not within 0 <= val < n
        for i, num in enumerate(nums):
            if not (0 <= num < n):
                nums[i] = 0
        # flag values as present without destroying them
        for i, num in enumerate(nums):
            nums[num % n] += n
        # iterate through nums and look for an index that is not flagged as present
        for i in range(1, n):
            if nums[i] < n:
                return i
        return n
    def firstMissingPositiveCheating(self, nums: List[int]) -> int:
        n, nums = len(nums), set(nums)
        for i in range(1, n + 2):
            if i not in nums:
                return i
        return n
