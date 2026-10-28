class Solution:
    def binaryGap(self, n: int) -> int:
        last_position=-1
        max_gap=0
        position=0
        while n>0:
            if n&1:
                if last_position!=-1:
                    max_gap=max(max_gap, position-last_position)
                last_position=position
            n>>=1
            position+=1
        return max_gap