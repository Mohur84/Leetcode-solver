class Solution:
    def checkStraightLine(self, coordinates):
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for x, y in coordinates[2:]:
            if (y - y1) * (x2 - x1) != (y2 - y1) * (x - x1):
                return False
        return True