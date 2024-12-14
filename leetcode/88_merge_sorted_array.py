from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1b = nums1[:m]
        index1, index2 = 0, 0
        for i in range(m + n):
            if index2 == n or index1 < m and nums1b[index1] < nums2[index2]:
                nums1[i] = nums1b[index1]
                index1 += 1
            else:
                nums1[i] = nums2[index2]
                index2 += 1
