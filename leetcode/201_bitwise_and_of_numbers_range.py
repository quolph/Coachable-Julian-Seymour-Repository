class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
    def rangeBitwiseAndSlow(self, left: int, right: int) -> int:
        common = left & right
        temp = common
        exp2 = 1
        while temp > 0:
            if temp & 1 == 1 and right - left >= exp2:
                common &= ~exp2
            exp2 *= 2
            temp >>= 1
        return common
