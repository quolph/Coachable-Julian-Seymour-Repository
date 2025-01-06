class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def missing(x):
            return nums[x] - nums[0] - x
        lo, hi = 0, len(nums) - 1
        if missing(hi) < k:
            return nums[hi] + k - missing(hi)
        while lo < hi:
            mid = (lo + hi)//2
            miss = missing(mid)
            if miss == k:
                mid -= 1
                while nums[mid + 1] == nums[mid] + 1:
                    mid -= 1
                return nums[mid] + k - missing(mid)
            elif miss < k:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo] + k - missing(lo) - 1
