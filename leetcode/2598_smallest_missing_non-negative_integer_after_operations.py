from typing import List
from collections import defaultdict

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counter = [0] * value
        for num in nums:
            counter[num % value] += 1
        mini = min(counter)
        for num, count in enumerate(counter):
            if count == mini:
                return mini * value + num
        return mini * value + 1
    def findSmallestIntegerSlow(self, nums: List[int], value: int) -> int:
        if value == 1:
            return len(nums)
        uniques = defaultdict(int)
        for num in nums:
            uniques[num] += 1
        counter = defaultdict(int)
        for i, num in enumerate(nums):
            if num < 0:
                num = -num % value
                if num != 0:
                    num = value - num
            else:
                num %= value
            counter[num] += 1
        for i in range(len(nums)):
            if i not in counter:
                return i
            if counter[i] > 1:
                num = i
                while counter[i] > 1 and num < len(nums):
                    counter[i] -= 1
                    if counter[i] == 0:
                        counter.pop(i)
                    num += value
                    counter[num] += 1
        return len(nums)
