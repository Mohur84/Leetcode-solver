class Solution:
    def getSum(self, a, b):
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        a &= MASK
        b &= MASK
        for _ in range(32):
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK
            if b == 0:
                break
        if a <= MAX_INT:
            return a
        return ~(a ^ MASK)