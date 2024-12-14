from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_height = max(height)
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            max_area = max(max_area, width * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if width * max_height <= max_area:
                break
        return max_area
