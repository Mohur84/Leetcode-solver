class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid={'0','1','2','5','6','8','9'}
        changed={'2','5','6','9'}
        count=0
        for num in range(1, n+1):
            s=str(num)
            if all(d in valid for d in s) and any(
                d in changed for d in s
            ):
                count+=1
        return count