class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_angle=minutes*6
        hour_angle=(hour%12)*30+minutes*0.5
        difference=abs(hour_angle-minutes_angle)
        return min(difference, 360-difference)