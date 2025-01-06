from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x1 = x2 = mask = 0
        for num in nums:
            x1 ^= x2 & num
            x2 ^= num
            mask = ~(x1 & x2)
            x1 &= mask
            x2 &= mask
        return x2
    def singleNumberCheating2(self, nums: List[int]) -> int:
        candidates, disqualified = set(), set()
        for num in nums:
            if num in disqualified:
                continue
            if num in candidates:
                candidates.remove(num)
                disqualified.add(num)
            else:
                candidates.add(num)
        for num in candidates:
            return num
    def singleNumberCheating(self, nums: List[int]) -> int:
        for key, value in Counter(nums).items():
            if value == 1:
                return key
        return math.inf
