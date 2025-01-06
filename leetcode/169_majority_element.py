from typing include List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 0
        majority = 0
        for num in nums:
            if counter == 0:
                majority = num
            if num == majority:
                counter += 1
            else:
                counter -= 1
        return majority
    def majorityElementBad2(self, nums: List[int]) -> int:
        n = len(nums)
        majority = n//2
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            if counter[num] > majority:
                return num
        return -1
    def majorityElementBad(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter(nums)
        for key, count in counter.items():
            if count > n/2:
                return key
        return -1
