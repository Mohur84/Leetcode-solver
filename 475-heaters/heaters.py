class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        radius=0
        for house in houses:
            i=bisect_left(heaters, house)
            left_dist=(
                house-heaters[i-1] if i>0 else float('inf')
            )
            right_dist=(
                heaters[i]-house if i<len(heaters) else float('inf')
            )
            radius=max(radius, min(left_dist, right_dist))
        return radius