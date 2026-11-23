class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        max_reach=[0]*(n+1)
        for i in range(n+1):
            left=max(0, i-ranges[i])
            right=min(n, i+ranges[i])
            max_reach[left]=max(max_reach[left], right)
        taps=0
        current_end=0
        farthest=0
        for i in range(n+1):
            if i>farthest:
                return -1
            farthest=max(farthest, max_reach[i])
            if i==current_end:
                if current_end==n:
                    break
                taps+=1
                current_end=farthest
        return taps