from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        to_left, to_right = 0, 0
        answer = 0
        while left < right:
            if height[left] < height[right]:
                answer += max(0, to_left - height[left])
                to_left = max(to_left, height[left])
                left += 1
            else:
                answer += max(0, to_right - height[right])
                to_right = max(to_right, height[right])
                right -= 1
        return answer
    def trapWastesMemory(self, height: List[int]) -> int:
        to_right = [0] * len(height)
        for i in range(len(height) - 2, -1, -1):
            to_right[i] = max(to_right[i + 1], height[i + 1])
        to_left = 0
        answer = 0
        for i in range(len(height)):
            if i > 0:
                to_left = max(to_left, height[i - 1])
            max_water = min(to_left, to_right[i])
            answer += max(0, max_water - height[i])
        return answer
