class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxx = max(weights)
        lo = max(ceil(sum(weights)/days), maxx)
        hi = min(lo + maxx, ceil(len(weights)/days) * maxx)
        #print(str((maxx, sum(weights))))
        #print(str((lo, hi)))
        def possible(capacity: int) -> bool:
            i = 0
            days_passed = 0
            while i < len(weights) and days_passed < days:
                weight = 0
                while i < len(weights) and weight + weights[i] <= capacity:
                    weight += weights[i]
                    i += 1
                days_passed += 1
            if i < len(weights):
                return False
            return True
        while lo < hi:
            mid = (lo + hi)//2
            if possible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
