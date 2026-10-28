class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g=gcd(p, q)
        p//=g
        q//=g
        if p%2==0:
            return 2
        if q%2==0:
            return 0
        return 1