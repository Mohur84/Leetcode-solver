class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits=sorted(str(n))
        power=1
        while len(str(power))<=len(str(n)):
            if sorted(str(power))==digits:
                return True
            power*=2
        return False