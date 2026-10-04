class Solution:
    def canMeasureWater(self, x, y, target):
        if target>x+y:
            return False
        if target==0:
            return True
        return target%gcd(x, y)==0