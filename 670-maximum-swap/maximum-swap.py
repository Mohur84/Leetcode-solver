class Solution:
    def maximumSwap(self, num: int) -> int:
        digits=list(str(num))
        last=[-1]*10
        for i, digit in enumerate(digits):
            last[int(digit)]=i
        for i, digit in enumerate(digits):
            current=int(digit)
            for d in range(9, current, -1):
                if last[d]>i:
                    digits[i], digits[last[d]]=digits[last[d]], digits[i]
                    return int("".join(digits))
        return num