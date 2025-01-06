class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_of_hour = (hour % 12) * 30 + 30 * (minutes/60)
        angle_of_minutes = 6 * minutes
        answer = abs(angle_of_hour - angle_of_minutes)
        return min(answer, 360 - answer)
