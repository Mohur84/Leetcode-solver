class Solution:
    def numMovesStonesII(self, stones: list[int]) -> list[int]:
        stones.sort()
        n=len(stones)
        n=len(stones)
        max_moves=max(
            stones[n-2]-stones[0],
            stones[n-1]-stones[1]
        )-(n-2)
        min_moves=n
        j=0
        for i in range(n):
            while stones[i]-stones[j]+1>n:
                j+=1
            already=i-j+1
            if already==n-1 and stones[i]-stones[j]==n-2:
                min_moves=min(min_moves, 2)
            else:
                min_moves=min(min_moves, n-already)
        return [min_moves, max_moves]